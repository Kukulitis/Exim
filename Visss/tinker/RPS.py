from tkinter import *
from tkinter import messagebox
from tkinter import filedialog
from tkinter import ttk

def rockPaperScissors(player):
    print(player)
    
window=Tk()
window.geometry('800x800')
window.title("Rock,Paper,Scissors")
window.config(background="pink")



rock = Button(window,
                 font=("Visby",13, "bold"),
                 text="Rock",
                 background="#C0C0C0",
                 activebackground="#808080",
                 command=rockPaperScissors("rock"))

paper = Button(window,
                 font=("Visby",13, "bold"),
                 text="Paper",
                 background="#C0C0C0",
                 activebackground="#808080",
                 command=rockPaperScissors("paper"))

scissors = Button(window,
                 font=("Visby",13, "bold"),
                 text="Scissors",
                 background="#C0C0C0",
                 activebackground="#808080",
                 command=rockPaperScissors("scissors"))

rock.place(x=93,y=150)
paper.place(x=90,y=200)
scissors.place(x=80,y=250)

window.mainloop()