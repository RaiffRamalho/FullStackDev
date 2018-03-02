class Parent():
	def __init__(self, last_name, eye_color):
		self.last_name = last_name
		self.eye_color = eye_color
		
	def show_info(self):
		print("last_name "+ self.last_name)

class Son(Parent):
	def __init__(self, last_name, eye_color, toys):
		Parent.__init__(self, last_name, eye_color)
		self.toys = toys
	
	def show_info(self):
		print("toys "+ str(self.toys))

son_bill = Son("cid","brown", 4)
son_bill.show_info()