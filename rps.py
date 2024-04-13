from tkinter import *
import random

root = Tk()
root.geometry("400x300")
root.title("Rock Paper Scissors Game")

computer_value = {
    "0": "Rock",
    "1": "Paper",
    "2": "Scissor"
}

user_wins = 0
computer_wins = 0
game_over = False

def enable_buttons():
    b1["state"] = "active"
    b2["state"] = "active"
    b3["state"] = "active"

def disable_buttons():
    b1["state"] = "disabled"
    b2["state"] = "disabled"
    b3["state"] = "disabled"

def update_scoreboard():
    scoreboard.config(text=f"User: {user_wins}  Computer: {computer_wins}")

def isrock():
    global user_wins, computer_wins, game_over
    if not game_over:
        user_choice = "Rock"
        c_v = computer_value[str(random.randint(0, 2))]
        if c_v == "Rock":
            match_result = "Match Draw"
        elif c_v == "Scissor":
            match_result = "Player Win"
            user_wins += 1
        else:
            match_result = "Computer Win"
            computer_wins += 1
        display_results(user_choice, c_v, match_result)

def ispaper():
    global user_wins, computer_wins, game_over
    if not game_over:
        user_choice = "Paper"
        c_v = computer_value[str(random.randint(0, 2))]
        if c_v == "Paper":
            match_result = "Match Draw"
        elif c_v == "Scissor":
            match_result = "Computer Win"
            computer_wins += 1
        else:
            match_result = "Player Win"
            user_wins += 1
        display_results(user_choice, c_v, match_result)

def isscissor():
    global user_wins, computer_wins, game_over
    if not game_over:
        user_choice = "Scissor"
        c_v = computer_value[str(random.randint(0, 2))]
        if c_v == "Rock":
            match_result = "Computer Win"
            computer_wins += 1
        elif c_v == "Scissor":
            match_result = "Match Draw"
        else:
            match_result = "Player Win"
            user_wins += 1
        display_results(user_choice, c_v, match_result)

def display_results(user_choice, computer_choice, match_result):
    disable_buttons()
    l1.config(text=f"Player: {user_choice}\t")
    l3.config(text=f"Computer: {computer_choice}")
    l4.config(text=match_result)
    update_scoreboard()
    root.after(1000, reset_game)  # Automatically reset the game after 2 seconds

def quit_game():
    global game_over
    game_over = True

def reset_game():
    global user_wins, computer_wins, game_over
    user_wins = 0
    computer_wins = 0
    update_scoreboard()
    enable_buttons()
    game_over = False

Label(root, text="Rock Paper Scissor", font="normal 20 bold", fg="blue").pack(pady=20)

frame = Frame(root)
frame.pack()

l1 = Label(frame, text="Player\t", font=10)
l2 = Label(frame, text="VS\t", font="normal 10 bold")
l3 = Label(frame, text="Computer", font=10)

l1.pack(side=LEFT)
l2.pack(side=LEFT)
l3.pack()

l4 = Label(root, text="", font="normal 20 bold", bg="white", width=15, borderwidth=2, relief="solid")
l4.pack(pady=20)

frame1 = Frame(root)
frame1.pack()

b1 = Button(frame1, text="Rock", font=10, width=7, command=isrock)
b2 = Button(frame1, text="Paper", font=10, width=7, command=ispaper)
b3 = Button(frame1, text="Scissor", font=10, width=7, command=isscissor)

b1.pack(side=LEFT, padx=10)
b2.pack(side=LEFT, padx=10)
b3.pack(padx=10)

scoreboard = Label(root, text=f"User: {user_wins}  Computer: {computer_wins}", font=10)
scoreboard.pack()

Button(root, text="Quit Game", font=10, fg="red", bg="black", command=quit_game).pack(pady=20)

root.mainloop()
