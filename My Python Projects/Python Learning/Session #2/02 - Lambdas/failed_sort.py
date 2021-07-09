# This code will return an error because the sort method does not know
# which presenter field to use when sorting
presenters = [
    {'name': 'Jeff', 'age': 50},
    {'name': 'Cow', 'age': 47}
]

presenters.sort()
print(presenters)
