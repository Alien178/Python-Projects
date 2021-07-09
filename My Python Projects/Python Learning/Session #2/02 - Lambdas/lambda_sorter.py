presenters = [
    {'name': 'Jeff', 'age': 50},
    {'name': 'Cow', 'age': 47}
]

presenters.sort(key=lambda item: item['name'])
print('-- alphabetically --')
print(presenters)

presenters.sort(key=lambda item: len(item['name']))
print('-- length --')
print(presenters)

