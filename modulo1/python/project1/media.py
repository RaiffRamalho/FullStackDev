import webbrowser

class Movie():

	"""Movie class with informations of title, storyline, image and trailer"""

	def __init__(self, movie_title, movie_storyline, poster_image, trailer_youtube):
		self.title = movie_title
		self.storyline = movie_storyline
		self.poster_image_url = poster_image
		self.trailer_youtube_url = trailer_youtube
		
	"""Method to show trailer of the class"""
	def show_trailer(self):
		webbrowser.open(self.trailer_youtube_url)
		





