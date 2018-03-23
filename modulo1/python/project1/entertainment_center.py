import media, fresh_tomatoes


toy_story = media.Movie("toy story",
						"some history",
						"https://upload.wikimedia.org/wikipedia/pt/d/dc/Movie_poster_toy_story.jpg",
						"https://www.youtube.com/watch?v=Ny_hRfvsmU8")

avatar = media.Movie("avatar",
						"avatar story",
						"https://upload.wikimedia.org/wikipedia/pt/b/b0/Avatar-Teaser-Poster.jpg",
						"https://www.youtube.com/watch?v=5PSNL1qE6VY")

fast = media.Movie("fast and furious",
						"car story",
						"https://upload.wikimedia.org/wikipedia/pt/f/f9/TheFastandtheFurious.jpg",
						"https://www.youtube.com/watch?v=4bEMXlQXiS0")

movies = [toy_story, avatar, fast]
fresh_tomatoes.open_movies_page(movies)
