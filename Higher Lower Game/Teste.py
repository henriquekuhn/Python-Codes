#Find a specific LIST index

for index, my_dict in enumerate(game_data):
        if my_dict == dict_exclude:
            del game_data[index]