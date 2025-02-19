import logging
import os
import psycopg2
import redis
import json
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import ApplicationBuilder, CommandHandler, CallbackQueryHandler
from dotenv import load_dotenv
import aiohttp
from bs4 import BeautifulSoup

# Cargar variables de entorno
load_dotenv()

# Configuración de logging: toma el nivel desde la variable de entorno LOG_LEVEL
log_level = os.getenv('LOG_LEVEL', 'INFO').upper()
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=getattr(logging, log_level, logging.INFO)
)

# Excluir mensajes de nivel INFO de httpx
class ExcludeInfoFilter(logging.Filter):
    def filter(self, record):
        return record.levelno != logging.INFO

httpx_logger = logging.getLogger("httpx")
httpx_logger.addFilter(ExcludeInfoFilter())

# Helper: Quitar dominio de la URL para que el callback_data sea corto
def shorten_url(url):
    domain = "https://tablademareas.com"
    if url.startswith(domain):
        return url[len(domain):]
    return url

# Conexión a Redis
try:
    REDIS_PASSWORD = os.getenv('REDIS_PASSWORD')
    r = redis.Redis(
        host='tablamareas-redis', port=6379, db=0,
        password=REDIS_PASSWORD, decode_responses=True
    )
    logging.info("✅ Conectado a Redis")
except Exception as e:
    logging.error(f"⚠️  Error conectando a Redis: {e}")
    r = None

# Funciones de caché
def cache_set(key, value, expire=3600):
    if r:
        r.set(key, json.dumps(value), ex=expire)
        logging.info(f"🗃️ Guardado en caché: {key}")

def cache_get(key):
    if r:
        data = r.get(key)
        if data:
            logging.info(f"💾 Cache HIT para {key}")
            return json.loads(data)
        logging.info(f"🚫 Cache MISS para {key}")
    return None

# Conexión a PostgreSQL
DATABASE_URL = os.getenv('DATABASE_URL')
def get_db_connection():
    try:
        conn = psycopg2.connect(DATABASE_URL)
        return conn
    except Exception as e:
        logging.error(f"❌ Error conectando a PostgreSQL: {e}")
        return None

def init_db():
    conn = get_db_connection()
    if not conn:
        logging.error("⚠️ No se pudo inicializar la base de datos.")
        return
    with conn:
        with conn.cursor() as cur:
            cur.execute("""
                CREATE TABLE IF NOT EXISTS users (
                    id SERIAL PRIMARY KEY,
                    telegram_id BIGINT UNIQUE,
                    username TEXT,
                    first_name TEXT,
                    last_name TEXT
                );
            """)
            cur.execute("""
                CREATE TABLE IF NOT EXISTS events (
                    id SERIAL PRIMARY KEY,
                    user_id INTEGER REFERENCES users(id) ON DELETE CASCADE,
                    event_type TEXT,
                    event_data JSONB,
                    timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                );
            """)
    logging.info("✅ Base de datos inicializada correctamente.")

# Obtener token de Telegram
TELEGRAM_TOKEN = os.getenv('TELEGRAM_BOT_TOKEN')

# Función para obtener datos de la web con caché
async def fetch(url):
    url = url.split("#")[0]
    cached_data = cache_get(url)
    if cached_data:
        return cached_data
    async with aiohttp.ClientSession() as session:
        try:
            async with session.get(url, headers={"User-Agent": "Mozilla/5.0"}) as response:
                response.raise_for_status()
                text = await response.text()
                cache_set(url, text)
                return text
        except Exception as e:
            logging.error(f"❌ Error en fetch {url}: {e}")
            return None

# Función para registrar eventos
def log_user_event(telegram_id, event_type, event_data):
    conn = get_db_connection()
    if not conn:
        return
    with conn:
        with conn.cursor() as cur:
            cur.execute("""
                INSERT INTO events (user_id, event_type, event_data)
                VALUES ((SELECT id FROM users WHERE telegram_id = %s), %s, %s);
            """, (telegram_id, event_type, json.dumps(event_data)))
    logging.info(f"📝 Evento registrado: {event_type} - {event_data}")

# Comando /start
async def start(update: Update, context):
    user = update.message.from_user
    conn = get_db_connection()
    if conn:
        with conn:
            with conn.cursor() as cur:
                cur.execute("""
                    INSERT INTO users (telegram_id, username, first_name, last_name)
                    VALUES (%s, %s, %s, %s)
                    ON CONFLICT (telegram_id) DO NOTHING;
                """, (user.id, user.username, user.first_name, user.last_name))
    logging.info(f"👤 Nuevo usuario registrado: {user.username} ({user.id})")
    log_user_event(user.id, "start_command", {})
    await update.message.reply_text("¡Bienvenido! Soy un bot de tabla de mareas (https://tablademareas.com/).")
    await show_continents(update)

# Comando /reset
async def reset(update: Update, context):
    user = update.message.from_user
    conn = get_db_connection()
    if conn:
        with conn:
            with conn.cursor() as cur:
                cur.execute("""
                    DELETE FROM events WHERE user_id = (SELECT id FROM users WHERE telegram_id = %s);
                """, (user.id,))
    logging.info(f"🔄 Historial borrado para {user.username} ({user.id}).")
    log_user_event(user.id, "reset_command", {})
    await update.message.reply_text("Tu historial ha sido borrado.")

# Función para obtener continentes
async def show_continents(update: Update):
    full_url = "https://tablademareas.com/"
    response_text = await fetch(full_url)
    if response_text is None:
        await update.message.reply_text("Error al obtener los continentes.")
        return
    soup = BeautifulSoup(response_text, 'html.parser')
    continentes = soup.select('div#sitios_continentes a')

    keyboard = [[InlineKeyboardButton(c.text.strip(), callback_data=f"continent:{shorten_url(c['href'])}")]
                for c in continentes]
    logging.info(f"🌍 Mostrando continentes a {update.message.chat.username}({update.message.chat.id})")
    log_user_event(update.message.chat.id, "show_continents", {})
    await update.message.reply_text('Selecciona un continente:', reply_markup=InlineKeyboardMarkup(keyboard))

# Callback para continente: mostrar países
async def continent_callback(update: Update, context):
    query = update.callback_query
    await query.answer()
    short_url = query.data.split(":", 1)[1]
    full_url = "https://tablademareas.com" + short_url
    response_text = await fetch(full_url)
    if response_text is None:
        await query.edit_message_text("Error al obtener los países.")
        return
    soup = BeautifulSoup(response_text, 'html.parser')
    paises = soup.select('a.sitio_reciente_a')
    keyboard = [[InlineKeyboardButton(p.text.strip(), callback_data=f"country:{shorten_url(p['href'])}")]
                for p in paises]
    logging.info(f"🌎 {query.from_user.username} ({query.from_user.id}) seleccionó un continente")
    log_user_event(query.from_user.id, "continent_selected", {"url": full_url})
    await query.edit_message_text('Selecciona un país:', reply_markup=InlineKeyboardMarkup(keyboard))

# Callback para país: mostrar provincias y corregir mensaje
async def country_callback(update: Update, context):
    query = update.callback_query
    await query.answer()
    short_url = query.data.split(":", 1)[1]
    full_url = "https://tablademareas.com" + short_url
    response_text = await fetch(full_url)
    if response_text is None:
        await query.edit_message_text("Error al obtener las provincias.")
        return
    soup = BeautifulSoup(response_text, 'html.parser')
    provincias = soup.select('a.sitio_reciente_a')
    keyboard = [[InlineKeyboardButton(p.text.strip(), callback_data=f"province:{shorten_url(p['href'])}")]
                for p in provincias]
    logging.info(f"🚢 {query.from_user.username} ({query.from_user.id}) seleccionó un país")
    log_user_event(query.from_user.id, "country_selected", {"url": full_url})
    await query.edit_message_text('Selecciona una provincia:', reply_markup=InlineKeyboardMarkup(keyboard))

# Callback para provincia: mostrar puertos
async def province_callback(update: Update, context):
    query = update.callback_query
    await query.answer()
    short_url = query.data.split(":", 1)[1]
    full_url = "https://tablademareas.com" + short_url
    response_text = await fetch(full_url)
    if response_text is None:
        await query.edit_message_text("Error al obtener los puertos.")
        return
    soup = BeautifulSoup(response_text, 'html.parser')
    puertos = soup.select('a.sitio_estacion_a')
    if not puertos:
        await query.edit_message_text("No se encontraron puertos en la página.")
        return
    keyboard = [[InlineKeyboardButton(p.text.strip(), callback_data=f"port:{shorten_url(p['href'])}")]
                for p in puertos]
    logging.info(f"⚓ {query.from_user.username} ({query.from_user.id}) seleccionó una provincia")
    log_user_event(query.from_user.id, "province_selected", {"url": full_url})
    await query.edit_message_text('Selecciona un puerto:', reply_markup=InlineKeyboardMarkup(keyboard))

# Callback para puerto: acción final (mostrar enlace)
async def port_callback(update: Update, context):
    query = update.callback_query
    await query.answer()
    short_url = query.data.split(":", 1)[1]
    full_url = "https://tablademareas.com" + short_url
    logging.info(f"🚩 {query.from_user.username} ({query.from_user.id}) seleccionó un puerto")
    log_user_event(query.from_user.id, "port_selected", {"url": full_url})
    await query.edit_message_text(f"Enlace del puerto: {full_url}")

def main():
    app = ApplicationBuilder().token(TELEGRAM_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("reset", reset))
    app.add_handler(CallbackQueryHandler(continent_callback, pattern='^continent:'))
    app.add_handler(CallbackQueryHandler(country_callback, pattern='^country:'))
    app.add_handler(CallbackQueryHandler(province_callback, pattern='^province:'))
    app.add_handler(CallbackQueryHandler(port_callback, pattern='^port:'))
    logging.info("🤖 Iniciando el bot...")
    init_db()
    app.run_polling()

if __name__ == "__main__":
    main()
