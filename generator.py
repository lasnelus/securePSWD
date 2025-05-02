import string
import secrets
from tkinter import *
from tkinter import ttk

def generator(length:int, useDigits:bool=True, usePunctuation:bool=True) -> str:
    """
    Generates a random string of specified length using letters, digits, and punctuation.
    """
    characters = string.ascii_letters
    if useDigits==True:
        characters += string.digits 
    if usePunctuation==True:
        characters += string.punctuation
    return ''.join(secrets.choice(characters) for _ in range(length))


def generate_password():
    length_val = int(length.get())
    digits = Digits.get()
    punctuation = Ponctuation.get()
    password = generator(length_val, digits, punctuation)
    PSWD.set(password)


root = Tk()
root.title("Password Generator")
root.geometry("400x200")

mainframe = ttk.Frame(root, padding="10 10 10 10")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

length = StringVar()
Digits = BooleanVar()
Ponctuation = BooleanVar()
PSWD = StringVar()

ttk.Label(mainframe, text="Enter the length of the random PSWD:").grid(column=1, row=1, sticky=W)
length_entry = ttk.Entry(mainframe, width=7, textvariable=length)
length_entry.grid(column=2, row=1, sticky=(W, E))

ttk.Label(mainframe, text="Include digits?").grid(column=1, row=2, sticky=N)
ttk.Checkbutton(mainframe, variable=Digits).grid(column=2, row=2, sticky=W)

ttk.Label(mainframe, text="Include punctuation?").grid(column=1, row=3, sticky=N)
usePunctuation_check = ttk.Checkbutton(mainframe, variable=Ponctuation).grid(column=2, row=3, sticky=W)

ttk.Button(mainframe, text="generate", command=generate_password).grid(column=2, row=4, sticky=W)

ttk.Label(mainframe, text="Generated password:").grid(column=1, row=5, sticky=W)
ttk.Label(mainframe, textvariable=PSWD).grid(column=2, row=5, sticky=(W, E))

for child in mainframe.winfo_children():
    child.grid_configure(padx=5, pady=5)

length_entry.focus()
root.mainloop()