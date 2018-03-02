import time
import webbrowser

count = 0
while(count < 3):
	time.sleep(5)
	webbrowser.open("http://google.com")
	count = count + 1



