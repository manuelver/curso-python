import datetime


class Session:

    def __init__(self, chat_id, config, logger):
        self.logger = logger
        self.started = datetime.datetime.utcnow()
        self.chat_id = chat_id
        self.config = config
        self.expiration = self.config.SESSION_EXPIRATION_TIME
        self.players = {}
        self.status = ''
        self.messenger = None
        self.counter = datetime.datetime.utcnow()

    def player_add(self, player):
        if player.id not in self.players:
            self.players[player.id] = player
        else:
            self.update_log()
            raise ValueError('Ya está en la partida...')

    def player_quit(self, player):
        if player.id in self.players:
            del self.players[player.id]
        else:
            raise ValueError('no_está_en_la_partida')

    def end(self):
        self.ended = datetime.datetime.utcnow()

    def get_leaderboard(self):
        ldb = ''
        for player in self.players.values():
            ldb += f'{player.name} : {player.get_points()}\n'
        return ldb

    def set_messenger(self, messenger):
        self.messenger = messenger

    def update_timers(self):
        if self.status == 'running':
            elapsed = self.update_log()
            if elapsed.seconds > self.expiration:
                self.status = 'timed_out'

    def update_counter(self):
        self.counter = datetime.datetime.utcnow()
        self.logger.debug(f'{self.chat_id} : updater_counter: {self.counter}')

    def update_log(self):
        elapsed = datetime.datetime.utcnow() - self.counter
        self.logger.debug(f'{self.chat_id} : updater_timer: {elapsed}')
        return elapsed
