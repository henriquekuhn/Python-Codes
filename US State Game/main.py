import turtle
import os
import pandas

IMAGE = "blank_states_img.gif"
DIR = os.getcwd() + "/US State Game"
os.chdir(DIR)

x = 0

data_states = pandas.read_csv("50_states.csv")
list_of_states = data_states.state.to_list()
screen = turtle.Screen()

screen.title("U.S. States Game")
screen.addshape(IMAGE)
screen.setup(height=491, width=725)
turtle.shape(IMAGE)

# This code is used to build the csv file with the coordinate of each U.S. state
#def get_mouse_click_coor(x, y):
#    print(x, y)
#turtle.onscreenclick(get_mouse_click_coor)
#turtle.mainloop()

while(len(list_of_states)>0):
    answer_state = screen.textinput(title=f"{50 - len(list_of_states)}/50 - Guess the state", prompt="What's another state's name?").title()
    if answer_state in list_of_states:
        list_of_states.remove(answer_state)
        rosbiff = turtle.Turtle()
        rosbiff.hideturtle()
        rosbiff.penup() 
        state_data = data_states[data_states.state == answer_state]
        rosbiff.goto(int(state_data.x), int(state_data.y))
        rosbiff.write(answer_state)

    if answer_state == "Exit":
        missing_states = pandas.DataFrame(list_of_states)
        missing_states.to_csv("missing_states_to_learn.csv")
        break
