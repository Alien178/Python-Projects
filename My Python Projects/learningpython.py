#########################################################################
#Sunday
#########################################################################

# first_name = input("Please, \nEnter Your First Name\n")
# last_name = input("Please, \nEnter Your Last Name\n")

# output = f'Hello, \n{first_name} {last_name}'

# print(output)

# from datetime import datetime, timedelta

# # today = datetime.now()
# # print("Today is: " + str(today))

# birthday = input("When is your birthday (dd/mm/yyyy)?\n")

# birthday_date =  datetime.strptime(birthday, "%d/%m/%Y")


# print("Your Birthday is on " + str(birthday_date))

#########################################################################
#Monday
#########################################################################

# province = input("What province do you live in?\n")
# tax = 0
# if province == 'Alberta' \
#    or province == 'Nunavut':
# 	tax = 0.05
# elif province == 'Ontario':
# 	tax = 0.13
# else:
# 	tax = 0.15
# print(tax)

#########################################################################

# province = input("What province do you live in? ")
# tax = 0
# if province == 'Alberta' or province == 'Nunavut':
# 	tax = 0.05
# elif province == 'Ontario':
# 	tax = 0.13
# else:
# 	tax = 0.15
# print(tax)

#########################################################################

# country = input("What country do you live in? ")

# if country.lower() == 'canada':
# 	province = input("What province/state do you live in? ")
# 	if province in('Alberta',\
#        'Nunavut','Yukon'):
# 		tax = 0.05
# 	elif province == 'Ontario':
# 		tax = 0.13
# 	else:
# 		tax = 0.15
# else:
# 	tax = 0.0
# print(tax)

#########################################################################

# province = input("What province do you live in?\n")
# tax = 0
# if province in('Alberta','Nunavut','Yukon'):
# 	tax = 0.05
# elif province == 'Ontario':
# 	tax = 0.13
# else:
# 	tax = 0.15
# print(tax)

#########################################################################

# # I check to see if the requirements for honour roll are met
# gpa = float(input('What was your Grade Point Average? '))
# lowest_grade = float(input('What was your lowest grade? '))

# # Boolean variables allow you to remember a True/False value
# if gpa >= .85 and lowest_grade >= .70:
# 	honour_roll = True
# else:
# 	honour_roll = False

# # Somewhere later in your code if you need to check if students is 
# # on honour roll, all I need to do is check the boolean variable
# # I set earlier in my code
# if honour_roll:
# 	print('You made honour roll')
# else:
# 	print("You didn't make it in the honour roll")

# A student makes honour roll if their average is >=85
# and their lowest grade is not below .70
# gpa = float(input('What was your Grade Point Average? '))
# lowest_grade = input('What was your lowest grade? ')
# lowest_grade = float(lowest_grade)

# if gpa >= .85 and lowest_grade >= .70:
# 		print('You made the honour roll')

#########################################################################
#Tuesday
#########################################################################

# from datetime import datetime

# def print_time(task_name):
#     print(task_name)
#     print(datetime.now())
#     print()
# # print timestamps after each section of code
# # to see how long sections of code take to run

# first_name = 'Susan'
# print_time("Starting Task")


# for x in range(0,10):
#     print(x)
# print_time("Task Completed")

#########################################################################

# def get_initial(name):
#     initial = name[0:1]
#     return initial

# # Ask for a name and return the initials
# first_name = input('Enter your first name: ')
# first_name_initial = get_initial(first_name)

# middle_name = input('Enter your middle name: ')
# middle_name_initial = get_initial(middle_name)

# last_name = input('Enter your last name: ')
# last_name_initial = get_initial(last_name)

# print('Your initials are: ' + first_name_initial \
# 	+ middle_name_initial + last_name_initial)

#########################################################################

# # This function will take a name and return the 
# # Create a function to return the first initial of a name
# # Parameters:
# #   name: name of person
# # Return value
# #   first letter of name passed in
# def get_initial(name, force_uppercase = True):
#     if force_uppercase:
#         initial = name[0:1].upper()
#     else:
#         initial = name[0:1]
#     return initial

# # Ask for someone's name and return the initials
# first_name = input('Enter your first name: ')

# first_name_initial = get_initial(force_uppercase = False, name = first_name)

# print('Your initial is: ' + first_name_initial)

#########################################################################

