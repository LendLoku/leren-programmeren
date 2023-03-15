birds = [
    {'name': 'mus', 'key': 'm', 'count': 0},
    {'name': 'duif', 'key': 'd', 'count': 0},
    {'name': 'koolmees', 'key': 'k', 'count': 0},
    {'name': 'kraai', 'key': 'i', 'count': 0}
]

# print all birds with key and name
print('All birds:')
for bird in birds:
    print(f"{bird['key']} - {bird['name']}")

# define function to get bird by key
def get_bird_by_key(birds, key):
    for bird in birds:
        if bird['key'] == key:
            return bird
    return None

# repeat until given '.'
while True:
    key = input("Enter bird key (enter . to exit): ")
    if key == '.':
        break
    bird = get_bird_by_key(birds, key)
    if bird is not None:
        bird['count'] += 1
        print(f"{bird['name']} count: {bird['count']}")
    else:
        print("Invalid key. Please try again.")

# print all birds with name and count
print('Bird count:')
total_count = 0
for bird in birds:
    print(f"{bird['name']}: {bird['count']}")
    total_count += bird['count']

# print percentage of total count for each bird
print('Percentage of total count:')
for bird in birds:
    percentage = bird['count'] / total_count * 100 if total_count > 0 else 0
    print(f"{bird['name']}: {percentage:.2f}%")