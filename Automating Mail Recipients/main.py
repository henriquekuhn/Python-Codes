import os

DIRECTORY = os.getcwd() + "/Automating Mail Recipients"
os.chdir(DIRECTORY)

class recipient_mail:

    def __init__(self):
        self.name_list = []

    # Use the class variable directly, without 'self.'
    def get_recipients(self):
        with open("names.txt") as file:
            for line in file:
                self.name_list.append(line.strip())
        print(self.name_list)

    def save_mail(self):
        for name in self.name_list:
            with open(f"letter_for_{name}.txt", "w") as file:
                file.write(f"Dear {name},\n\n")
                file.write("I am chalanging you to a cheese run.\n\n")
                file.write("Hope you can face it!\n\n")
                file.write("Chuck Norris.")
            
                

write_mail = recipient_mail()
write_mail.get_recipients()
write_mail.save_mail()
