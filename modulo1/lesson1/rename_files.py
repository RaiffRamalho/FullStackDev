import os


def rename_file():
	path = r"C:\Users\raiffpc\Desktop\udacity\Lesson1\prank"
	fileNames = os.listdir(r"C:\Users\raiffpc\Desktop\udacity\Lesson1\prank")
	
	for file in fileNames:
		no_digits = []
		# Iterate through the string, adding non-numbers to the no_digits list
		for i in file:
			if not i.isdigit():
				no_digits.append(i)

		# Now join all elements of the list with '', 
		# which puts all of the characters together.
		result = ''.join(no_digits)
		print(os.path.join(path, result))

		os.rename(os.path.join(path, file), os.path.join(path, result))
	
	print(fileNames)
	
rename_file();