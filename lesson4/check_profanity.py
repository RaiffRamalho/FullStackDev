import urllib.request

def read_text():
	quotes = open(r"C:\Users\raiff\Desktop\fullStack\lesson4\movie_quotes.txt")
	content = quotes.read()
	quotes.close()
	check_profanity(content)
	
def check_profanity(text):
	connection = urllib.request.urlopen("http://www.wdylike.appspot.com/?q=shot")
	output = connection.read()
	print(output)
	connection.close()
	
	
read_text()