from storeman import *
import tkinter as tk
from tkinter import PhotoImage
import os

DEFAULT_BACKGROUND = "light grey"

def root_add_ingredient():
    # Read all characters from textbox, but no line break at the end (thus -1c)
    name = ingredient_name_textbox.get("1.0", "end-1c").strip()
    unit = ingredient_unit_textbox.get("1.0", "end-1c").strip()
    new_ingredient = {
        "name": name,
        "unit": unit
    }
    add_ingredient(new_ingredient)
    # Empty text boxes when finished
    ingredient_name_textbox.delete('1.0', "end")
    ingredient_unit_textbox.delete('1.0', "end")


root = tk.Tk()
root.title("HOLA FRIGO - A Hello Fresh Companion App")
root.geometry("800x800")
root.configure(bg=DEFAULT_BACKGROUND, padx=20, pady=20)

# Load, scale and display the logo image
logo_img = PhotoImage(file="./img/logo.png")
logo_img = logo_img.subsample(6, 6)
logo_img_label = tk.Label(root, image=logo_img, bg=DEFAULT_BACKGROUND)
logo_img_label.image = logo_img  # Keep a reference
logo_img_label.grid(row=0, column=0, sticky="nw", padx=10, pady=10)

# Heading Text label
heading_text_label = tk.Label(
    root,
    text="A Hello Fresh Companion App",
    font=("Helvetica", 20, "bold"),
    fg="black",
    bg=DEFAULT_BACKGROUND
)
heading_text_label.grid(row=0, column=1, sticky="w", padx=5, pady=5)

# Heading Text label
credits_text_label = tk.Label(
    root,
    text="created by\nSaaSpicious",
    font=("Helvetica", 12, "bold"),
    fg="dark grey",
    bg=DEFAULT_BACKGROUND
)
credits_text_label.grid(row=0, column=2, padx=10, pady=5)

# Add functionality to add new ingredient 
ingredient_heading_label = tk.Label(
    root,
    text="Ingredients",
    font=("Helvetica", 12, "bold"),
    fg="black",
    bg=DEFAULT_BACKGROUND
)
ingredient_heading_label.grid(row=1,column=0,columnspan=2)

ingredients_avl_label = tk.Label(
    root,
    text="Available:",
    font=("Helvetica", 10),
    fg="black",
    bg=DEFAULT_BACKGROUND
)
ingredients_avl_label.grid(row=2,column=0)
ingredients_available = get_sorted_ingredient_list()
ingredients_avl_list = tk.OptionMenu(root,*ingredients_available)
ingredients_avl_list.grid(row=2,column=1)

ingredient_name_label = tk.Label(
    root,
    text="Name:",
    font=("Helvetica", 10),
    fg="black",
    bg=DEFAULT_BACKGROUND
)
ingredient_name_label.grid(row=3,column=0)
ingredient_name_textbox = tk.Text(root,height=1,width=20)
ingredient_name_textbox.grid(row=3,column=1)

ingredient_unit_label = tk.Label(
    root,
    text="Unit:",
    font=("Helvetica", 10),
    fg="black",
    bg=DEFAULT_BACKGROUND
)
ingredient_unit_label.grid(row=4,column=0)
ingredient_unit_textbox = tk.Text(root,height=1,width=20)
ingredient_unit_textbox.grid(row=4,column=1)


add_ingredient_button = tk.Button(text="Add Ingredient",command=root_add_ingredient)
add_ingredient_button.grid(row=5, column=0,columnspan=2,pady=5)

root.mainloop()
