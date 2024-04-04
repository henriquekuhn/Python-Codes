# Demonstration of the advantage of the CLASS usage.

# Without CLASS
user_1_name = "Rosbiff"
user_1_id= 12345
user_1_age = 33

user_2_name = "Henrique"
user_2_id = 23456
user_2_age = 55

print(user_1_name)
print(user_2_name)


# With CLASS
class User: #CLASS
    def __init__(self, user_name, user_id, user_age):
        self.name = user_name
        self.id = user_id
        self.age = user_age
        self.followers = 0
        self.following = 0

    def follow(self, user): #METHOD
        user.followers += 1
        self.following += 1


class_user_1 = User("Rosbiff", 12345, 33)
class_user_2 = User("Henrique", 23456, 55)
print("#")
print(class_user_1.name)
print(class_user_2.name)
print("#")
class_user_1.follow(class_user_2)
print(f"User 1 following: {class_user_1.following}")
print(f"User 1 followers: {class_user_1.followers}")
print(f"User 2 following: {class_user_2.following}")
print(f"User 2 followers: {class_user_2.followers}")