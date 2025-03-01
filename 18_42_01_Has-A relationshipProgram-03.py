class SportNews:
    def getSportsinfo(self):
        print('Sports Information')


class MovieNews():
    def getMovieInfo(self):
        print('Movie Information')


class PoliticsNews():
    def getPoliticalInfo(self):
        print('Politics News')


class VarunNews:
    def __init__(self):
        self.sports = SportNews()
        self.movies = MovieNews()
        self.politics = PoliticsNews()

    def getTotalNews(self):
        print('welcome to varun News:')
        self.sports.getSportsinfo()
        self.movies.getMovieInfo()
        self.politics.getPoliticalInfo()


dnews = VarunNews()
dnews.getTotalNews()
