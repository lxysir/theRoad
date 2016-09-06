import webbrowser

class Video():
    def __init__(self, title, duration):
        self.title = title
        self.duration = duration

class Movie(Video):
    '''This is a introduce for the program'''
    
    VALID_RATINGS = ['G', 'G-13', 'P', 'R']
    
    def __init__(self, movie_title, movie_storyline, poster_image, trailer_youtube, duration):
        Video.__init__(self, movie_title, duration)
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)

class Tvshow(Video):
    def __init__(self, tv_title, season, episode, tv_station, duration):
        Video.__init__(self, tv_title, duration)
        self.season = season
        self.episode = episode
        self.tv_station = tv_station

    def get_local_listing(self):
        print(self.title)

escape = Tvshow("Escape", 7, "episode", "HBO", 120)
escape.get_local_listing()
