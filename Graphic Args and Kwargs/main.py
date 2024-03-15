from tkinter import *

window = Tk()
window.title("My first GUI program")
window.minsize(width=500, height=300)

#Label
my_label = Label(text="I am a Label", font=("Arial", 24, "bold"))
my_label.pack()

my_label["text"] = "New Label"
my_label.config(text="New Label")
 
def button_clicked():
    print("I got clicked")
    entry = input.get()
    my_label["text"] = entry

button = Button(text="click me", command=button_clicked)
button.pack()

input = Entry(width=10)
input.pack()






window.mainloop()