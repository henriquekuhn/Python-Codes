#Find a specific LIST index

data = [
    {
        'name': 'Instagram',
        'follower_count': 346,
        'description': 'Social media platform',
        'country': 'United States'
    },
    {
        'name': 'Cristiano Ronaldo',
        'follower_count': 215,
        'description': 'Footballer',
        'country': 'Portugal'
    }
]

print(data)
for index, my_dict in enumerate(data):
        if my_dict == data[0]:
            del data[index]
print(data)