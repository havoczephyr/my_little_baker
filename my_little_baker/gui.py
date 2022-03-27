import tkinter as tk
from tkinter import CENTER, ttk
from tkinter import filedialog as fd
from tkinter.messagebox import NO, showinfo
import json
from pprint import pprint

loaded_recipe = "NONE"

def gui():
    root = tk.Tk()
    root.iconbitmap("my_little_baker/static/bread.ico")

    root.title('My Little Baker')
    root.geometry('650x550')

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
        if filename != '':
            f = open(filename)
            recipe = json.load(f)
            loaded_recipe = recipe["main"][0]["name"]
            my_label.configure(text=f"Current Loaded Recipe: {loaded_recipe}")
            pprint(loaded_recipe)
            f.close()
        else:
            return
        
        def display_table():
            if loaded_recipe != 'NONE':
                recipe_table = tk.Frame(root)
                recipe_table.pack()
                recipe_tree = ttk.Treeview(recipe_table)
                column_list = []
                percentage = []

                for i in recipe['flours']:
                    column_list.append(i['name'])
                    percentage.append(i['percentage'])

                for i in recipe['ingredients']:
                    column_list.append(i['name'])
                    percentage.append(i['percentage'])
                
                column_list.append('Total')
                recipe_tree['columns'] = column_list

                recipe_tree.column("#0", width=0, stretch=NO)
                recipe_tree.heading("#0", text='', anchor=CENTER)
                for i in column_list:
                    recipe_tree.column(i, anchor=CENTER, width=80)
                    recipe_tree.heading(i, text=i, anchor=CENTER)

                recipe_tree.pack()
        display_table()


    open_button = ttk.Button(
            root,
            text='Open a Recipe JSON',
            command=select_file
        )
    open_button.pack()


    root.mainloop()