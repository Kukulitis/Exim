# import tkinter as tk

# logs=tk.Tk()
# logs.geometry("500x500")
# logs.title("tests")

# label=tk.Label(logs,text="Sup!")
# label.pack(padx=20,pady=20)

# tekstbox=tk.Text(logs,height=2)
# tekstbox.pack(padx=20,pady=20)
# # entry=tk.Entry(logs)
# # entry.pack
# button=tk.Button(logs, text="Supp?")
# button.pack(padx=10,pady=10)
# button.place(x=250,y=250,height=50,width=50)


# logs.mainloop()

import tkinter as tk
from tkinter import messagebox


class MyGUI:

    def __init__(self):
        self.root=tk.Tk()

        self.label=tk.Label(self.root)
        self.label.pack(padx=10,pady=10)

        self.textbox=tk.Text(self.root, height=3)
        self.textbox.pack(padx=10,pady=10)

        self.checkstate=tk.IntVar()


        self.check=tk.Checkbutton(self.root, text="Show me!",variable=self.checkstate)
        self.check.pack(padx=10,pady=10)

        self.button=tk.Button(text="Message",command=self.show_message)
        self.button.pack(padx=10,pady=10)

        self.root.mainloop()

    def show_message(self):
        if self.checkstate.get()==0:
            print(self.textbox.get('1.0',tk.END))
        else:
            messagebox.showinfo(title="Message", message=self.textbox.get('1.0',tk.END))

MyGUI() 
        