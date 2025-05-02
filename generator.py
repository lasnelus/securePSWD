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

def main():
    try:
        length = int(input("Enter the length of the random PSWD:"))
        useDigits = input("Include digits? (y/n): ").strip().lower() == 'y'
        password = generator(length, useDigits, usePunctuation)
        print(f"Generated password: {password}")
        usePunctuation = input("Include punctuation? (y/n): ").strip().lower() == 'y'
    except ValueError:
        print("Invalid input. Please enter a valid number for length.")

root = Tk()
root.title("Password Generator")
root.geometry("300x200")

mainframe = ttk.Frame(root, padding="3 3 12 12")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

length = StringVar()
feet_entry = ttk.Entry(mainframe, width=7, textvariable=length)
feet_entry.grid(column=2, row=1, sticky=(W, E))

meters = StringVar()
ttk.Label(mainframe, textvariable=meters).grid(column=2, row=2, sticky=(W, E))

ttk.Button(mainframe, text="Calculate", command=generator).grid(column=3, row=3, sticky=W)

ttk.Label(mainframe, text="Enter the length of the random PSWD:").grid(column=1, row=1, sticky=W)
ttk.Label(mainframe, text="Include digits?").grid(column=1, row=2, sticky=E)
ttk.Label(mainframe, text="Include punctuation?").grid(column=3, row=2, sticky=W)

for child in mainframe.winfo_children(): 
    child.grid_configure(padx=5, pady=5)

feet_entry.focus()
root.bind("<Return>", generator)

root.mainloop()
