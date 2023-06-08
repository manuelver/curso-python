import paramiko

# Crear una instancia del cliente SSH
client = paramiko.SSHClient()

# Configurar el cliente para aceptar automáticamente la clave del servidor
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

# Conectar al servidor SSH
client.connect(
    '192.168.1.1',
    port=666,
    username='admin',
    password='Passw0rd'
)

# Ejecutar comandos en el servidor
stdin, stdout, stderr = client.exec_command('ls')
output = stdout.read().decode()
print(output)

# Cerrar la conexión SSH
client.close()
