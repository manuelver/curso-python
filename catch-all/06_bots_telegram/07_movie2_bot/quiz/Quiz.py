from player.Player import Player
from random import choice
from collection.Collection import Collection
from miners.imdb.ImdbMiner import IMDB


class Quiz:
    movies_type = ''
    movie = None
    images = None

    def __init__(self, session):
        self.miner = IMDB()
        self.session = session

    def set_level(self, level):
        # Implementar el ajuste del nivel si es necesario
        pass

    def rand_movie(self, rand_type=None):
        collection = Collection(self.miner, rand_type)
        self.movie, self.images = collection.get_rand_movie()

    def get_movie_photo(self):
        if not self.images or 'images' not in self.images:
            raise ValueError("No images available")
        try:
            return choice(self.images['images'])['url']
        except (IndexError, KeyError) as e:
            raise ValueError("Error selecting image URL") from e

    def get_question(self, rand_type=None):
        try:
            self.rand_movie(rand_type)
            return self.get_movie_photo()
        except ValueError:
            return _("not_possible_find_movie")

    def show(self, update, rand_type):
        chat_id = update.message.chat_id
        try:
            movie_img = self.get_question(rand_type)
            self.session.messenger.send_msg(chat_id, "movie_bot", "title")
            self.session.messenger.send_photo(
                chat_id, movie_img, caption=_("question_which_movie")
            )
            self.session.updater_counter()
            self.session.status = "running"
        except ValueError as e:
            self.session.messenger.send_msg(
                chat_id,
                msg=_("error_fetching_question"),
                type_msg="bold"
            )
            self.session.status = "stopped"

    def check_resps(self, update):
        chat_id = update.message.chat_id
        if not self.movie or 'base' not in self.movie or 'title' not in self.movie['base']:
            self.session.messenger.send_msg(
                chat_id,
                msg=_("error_movie_data"),
                type_msg="bold"
            )
            return

        if str.lower(self.movie['base']['title']) == str.lower(update.message.text):
            player = Player(update.message.from_user.id)
            player.name = f"{update.message.from_user.first_name} {update.message.from_user.last_name}"
            try:
                self.session.player_add(player)
            except ValueError:
                pass

            self.session.players[update.message.from_user.id].add_points(1)
            self.session.messenger.send_msg(
                chat_id,
                msg=(player.name, _("correct_answer")),
                type_msg="bold"
            )
            self.movie = None
            self.session.status = "stopped"

    def check_expiration(self):
        try:
            self.session.update_timer()
        except ValueError:
            pass

        if self.session.status == "timed_out":
            self.session.messenger.send_msg(
                chat_id=self.session.chat_id,
                msg=_("times_up", self.movie['base']
                      ['title'] if self.movie else ""),
                type_msg="bold"
            )
            self.session.status = "stopped"
            self.movie = None
