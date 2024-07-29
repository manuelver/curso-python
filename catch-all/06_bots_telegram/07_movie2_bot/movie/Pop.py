from movie.Movie import Movie


class Pop(Movie):

    def __init__(self):
        super(Pop, self).__init__(name='Pop Movie')
        self.type = "pop"
