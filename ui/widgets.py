from customtkinter import *

def create_labeled_entry(parent, text, row):
    label = CTkLabel(parent, text=text)
    label.grid(row=row, column=0, padx=10, pady=5, sticky="e")

    entry = CTkEntry(parent)
    entry.grid(row=row, column=1, padx=10, pady=5, sticky="w")

    return entry
