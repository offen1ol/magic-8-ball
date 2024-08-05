# https://web.archive.org/web/20180612183650/https://github.com/jorgegonzalez/beginner-projects#magic-8-ball

# bonus: 
#   add a gui
#   it must have a box for users to enter the question
#   it must have at least 4 buttons: 
#       ask
#       clear (the text box)
#       play again
#       quit (this must close the window)

'''
How to activate your venv in command line: source .venv/bin/activate
How to deactivate your venv in command line: deactivate
'''

'''
when you run your file you need to use 'python3 [file name]' not 'python [file name]' so that it runs the newer version of tkinter
tkinter 8.5 = bad (throws a deprecated warning message)
tkinter 8.6 = good (no warning thrown)
'''

''' 
UPDATE: No idea how to install tkinter version in venv. It uses it through my local computer. 
But hey! It works through brew ig...
'''

import tkinter as tk
import ttkbootstrap as ttk
import random

def clear():
    print("cleared textbox")
    entry_string.set("")

def think():
    print("Thinking...")
    answer_string.set("Thinking...")

# function to check if the entry box is empty, throw error message if true
def check_question(question):
    if len(str(question)) == 0:
        answer_string.set("I didn't see a question...")
        create_menu_frame()
        disable_buttons()
        print("There is no question")  
    else:
        # call disable_buttons
        disable_buttons()
        think()
        answer_label.after(5000, answer, random.randrange(1,20))

# disable buttons once "ask" button is clicked
def disable_buttons():
    entry_box["state"] = "disabled"
    clear_button["state"] = "disabled"
    ask_button["state"] = "disabled"
    
def enable_buttons():
    entry_box["state"] = "enabled"
    clear_button["state"] = "enabled"
    ask_button["state"] = "enabled"

# create menu button frame each time
def create_menu_frame(): 
    menu_frame = ttk.Frame(master = window)
    menu_frame.pack()

    # replay button
    replay_button = ttk.Button(master = menu_frame, text = "Play Again", command = lambda: [
        menu_frame.destroy(), 
        enable_buttons(), 
        answer_string.set(""), 
        clear(),
        ])
    replay_button.pack(side = "left", padx = 10)

    # quit button
    quit_button = ttk.Button(master = menu_frame, text = "Quit", command = lambda: window.destroy())
    quit_button.pack(side = "left", padx = 10)

def answer(num): 
    responses = {
        1: "It is certain",
        2: "It is decidedly so",
        3: "Without a doubt",
        4: "Yes, definitely",
        5: "You may rely on it",
        6: "As I see it, yes",
        7: "Most likely",
        8: "Outlook good",
        9: "Yes",
        10: "Signs point to yes",
        11: "Reply hazy, try again...",
        12: "Ask again later",
        13: "Better not tell you now...",
        14: "Cannot predict now",
        15: "Concentrate and ask again",
        16: "Don't count on it",
        17: "My reply is no",
        18: "My sources say no",
        19: "Outlook not so good",
        20: "Very doubtful"
    }

    print(responses[num])
    answer_string.set(responses[num])

    # call create_menu_frame()
    create_menu_frame()

# create gui window
window = ttk.Window(themename = "vapor")

# window title
window.title("Magic 8 Ball")

# window dimension
window.geometry("350x200")

# input frame
input_frame = ttk.Frame(master = window)
input_frame.pack(pady = 15)

# menu title
header_title = ttk.Label(master = input_frame,
                       text = "What would you like to know?",
                       font = "Arial 18")
header_title.pack(pady = 5)

# answer 
answer_string = tk.StringVar()
answer_label = ttk.Label(master = window,
                         text = "Answer",
                         textvariable = answer_string,
                         font = "Arial 18 bold")
answer_label.pack(pady = 10)

# textbox and clear button
entry_string = tk.StringVar()
entry_box = ttk.Entry(master = input_frame, 
                      textvariable = entry_string)

clear_button = ttk.Button(master = input_frame, 
                          text = "Clear", 
                          command = lambda: clear())
ask_button = ttk.Button(master = input_frame, 
                        text = "Ask", 
                        command = lambda: check_question(entry_string.get()))

entry_box.pack(side = "left")
clear_button.pack(side = "left")
ask_button.pack(side = "left")

# run window
window.mainloop()