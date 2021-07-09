class Presenter():
	def __init__(self, name):
		# Constructor
		self.name = name

	@property
	def name(self):
		print('Retrieving name...')
		return self.__name
	@name.setter
	def name(self, value):
		# cool validation here
		print('Validating name...')
		self.__name = value

presenter = Presenter('Aayush')
presenter.name = 'Aayush'
print(presenter.name)