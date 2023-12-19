import turtle
import pandas
from print import Print
import numpy

screen=turtle.Screen()
to_print=Print()
screen.title("U.S. States Same")
image="blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
data= pandas.read_csv("50_states.csv")
correct_answers=[]
all_state=data.state.to_list()
while len(correct_answers) != 50:
    user_answer= screen.textinput(title=f"{len(correct_answers)}/50 States Correct", prompt="What's another state name?").title()
    if user_answer== "Exit":
        to_learn = [state for state in all_state if state not in correct_answers]
        new_data = pandas.DataFrame(to_learn)
        new_data.to_csv("States_to_learn.csv")
        break
    if user_answer in all_state:
        state_row= data[data.state == user_answer]
        state_x=state_row.x.iloc[0]
        state_y=state_row.y.iloc[0]
        to_print.print_state(state_x,state_y,user_answer)
        correct_answers.append(user_answer)



