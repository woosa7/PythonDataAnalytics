import webbrowser

class Movie():
    def __init__(self, mtitle, mstory, posterUrl, trailerUrl):
        self.title = mtitle
        self.story = mstory
        self.posterUrl = posterUrl
        self.trailerUrl = trailerUrl

    def show_trailer(self):
        webbrowser.open(self.trailerUrl)