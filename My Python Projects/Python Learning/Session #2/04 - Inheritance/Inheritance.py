class Person:
	def __init__(self, name):
		self.name = name
	def say_hello(self):
		print('Hello, ' + self.name)
		print("Trasfering: \nElementry School to Junior High School")

class Student(Person):
	def __init__(self, name, school):
		super().__init__(name)
		self.school = school
	def school_transfer(self):
		print('IV to ' + self.school)

student = Student('Aayush Kokate', 'GVJH')
student.say_hello()
student.school_transfer()
# What are you?
print(isinstance(student, Student))
print(isinstance(student, Person))
print(issubclass(Student, Person))
