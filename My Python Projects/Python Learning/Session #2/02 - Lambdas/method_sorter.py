def sorter(item):
    return item['name']


presenters = [
    {'name': 'Jeff', 'age': 50},
    {'name': 'Cow', 'age': 47}
]
presenters.sort(key=sorter)
print(presenters)
