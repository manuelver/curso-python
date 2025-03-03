from abc import ABCMeta, abstractmethod


class Miner(object):

    __metaclass__ = ABCMeta

    handle = None

    @abstractmethod
    def top_list(self, number):
        pass

    @abstractmethod
    def get_movie_id(self, index):
        pass

    @abstractmethod
    def get_movie_by_id(self, movie_id):
        pass
