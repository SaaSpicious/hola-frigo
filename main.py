import tkinter as tk
from tkinter import PhotoImage
import os

DEFAULT_BACKGROUND = "light grey"

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

root.mainloop()
