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

    # additional button frame
    menu_frame = ttk.Frame(master = window)
    menu_frame.pack()

    # replay button
    replay_button = ttk.Button(master = menu_frame, text = "Play Again")
    replay_button.pack(side = "left")

    # quit button
    quit_button = ttk.Button(master = menu_frame, text = "Quit")
    quit_button.pack(side = "left")



# def main():
#     # ask = str(input("What would you like to know?\n")).lower()
#     ask = 0

#     # while ask != "quit":
#     #     answer(random.randrange(1,20))

#     #     ask = str(input("What else would you like to know?\n")).lower()
    

# if __name__ == '__main__':
#     main()

# create gui window
window = ttk.Window(themename = "morph")

# window title
window.title("Magic 8 Ball")

# window dimension
window.geometry("350x200")

# menu title
header_title = ttk.Label(master = window,
                       text = "What would you like to know?",
                       font = "Arial 18")
header_title.pack()

# input frame
input_frame = ttk.Frame(master = window)
input_frame.pack()

# answer 
answer_string = tk.StringVar()
answer_label = ttk.Label(master = window,
                         text = "Answer",
                         textvariable = answer_string,
                         font = "Arial 18 bold")
answer_label.pack()

# textbox and clear button
entry_string = tk.StringVar()
entry_box = ttk.Entry(master = input_frame, 
                      textvariable = entry_string)

clear_button = ttk.Button(master = input_frame, 
                          text = "Clear", 
                          command = lambda: clear())
ask_button = ttk.Button(master = input_frame, 
                        text = "Ask", 
                        command = lambda: [think(), answer_label.after(5000, answer, random.randrange(1,20))])

entry_box.pack(side = "left")
clear_button.pack(side = "left")
ask_button.pack(side = "left")

# run window
window.mainloop()

