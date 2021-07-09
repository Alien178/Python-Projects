class Presenter():
	def __init__(self, name):
		# Constructor
		self.name = name
	def say_hello(self):
		# method
		print('Hello, ' + self.name)

presenter = Presenter('AAK')
presenter.name = 'Aayush'
presenter.say_hello()