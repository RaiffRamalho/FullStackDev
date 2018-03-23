import urllib.request

def read_text():
	quotes = open(r"C:\Users\raiff\Desktop\fullStack\lesson4\movie_quotes.txt")
	content = quotes.read()
	quotes.close()
	check_profanity(content)
	
def check_profanity(text):
	connection = urllib.request.urlopen("http://www.wdylike.appspot.com/?q="+ urllib.request.quote(text))
	output = connection.read()
	print(output)
	connection.close()
	if 'false' in output:
		print("no")
	elif 'true' in output:
		print("yes")
	else:
		print("can not do")
	
	
read_text()