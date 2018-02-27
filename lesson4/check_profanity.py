import urllib

def read_text():
	quotes = open(r"C:\Users\raiff\Desktop\fullStack\lesson4\movie_quotes.txt")
	content = quotes.read()
	print(content)
	quotes.close()
	check_profanity(content)
	
def check_profanity(text):
	connection = urllib.urlopen("http://www.wdylike.appspot.com/?q="+text)
	output = connection.read()
	print(output)
	connection.close
	
read_text()