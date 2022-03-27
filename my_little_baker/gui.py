import tkinter as tk
from tkinter import ttk
from tkinter import filedialog as fd
from tkinter.messagebox import showinfo
import json
from pprint import pprint

loaded_recipe = "NONE"

def gui():
    root = tk.Tk()
    root.iconbitmap("my_little_baker/static/bread.ico")

    root.title('My Little Baker')
    root.resizable(False, False)
    root.geometry('300x150')

    my_label = ttk.Label(root, text=f"Current Loaded Recipe: {loaded_recipe}")
    my_label.pack()


    def select_file():
        filetypes = (
            ('JSON', '*.json'),
            ('All files', "*.*")
        )

        filename = fd.askopenfilename(
            title='Open a Recipe JSON',
            initialdir='/',
            filetypes=filetypes)

        showinfo(
            title='Recipe Loaded',
            message=f"Recipe {filename} has been loaded"
        )
        f = open(filename)
        recipe = json.load(f)
        loaded_recipe = recipe["main"][0]["name"]
        my_label.configure(text=f"Current Loaded Recipe: {loaded_recipe}")
        pprint(loaded_recipe)
        f.close()

    open_button = ttk.Button(
            root,
            text='Open a Recipe JSON',
            command=select_file
        )
    open_button.pack()



    root.mainloop()