import tkinter as tk
from tkinter import messagebox

def text_to_binary_hex():
    text = text_entry.get()
    if text:
        binary_result.set(' '.join(format(ord(c), '08b') for c in text))
        hex_result.set(' '.join(format(ord(c), '02X') for c in text))
    else:
        messagebox.showwarning("Input Error", "Please enter text to convert.")

def binary_to_text():
    try:
        binary = binary_entry.get()
        text = ''.join(chr(int(b, 2)) for b in binary.split())
        text_entry.delete(0, tk.END)
        text_entry.insert(0, text)
        text_to_binary_hex()
    except ValueError:
        messagebox.showerror("Conversion Error", "Invalid binary format.")

def hex_to_text():
    try:
        hex_str = hex_entry.get()
        text = ''.join(chr(int(h, 16)) for h in hex_str.split())
        text_entry.delete(0, tk.END)
        text_entry.insert(0, text)
        text_to_binary_hex()
    except ValueError:
        messagebox.showerror("Conversion Error", "Invalid hexadecimal format.")

root = tk.Tk()
root.title("Text Converter")

# Text Input
tk.Label(root, text="Enter Text:").grid(row=0, column=0)
text_entry = tk.Entry(root, width=50)
text_entry.grid(row=0, column=1)
tk.Button(root, text="Convert", command=text_to_binary_hex).grid(row=0, column=2)

# Binary Output
binary_result = tk.StringVar()
tk.Label(root, text="Binary:").grid(row=1, column=0)
binary_entry = tk.Entry(root, textvariable=binary_result, width=50)
binary_entry.grid(row=1, column=1)
tk.Button(root, text="To Text & Hex", command=binary_to_text).grid(row=1, column=2)

# Hex Output
hex_result = tk.StringVar()
tk.Label(root, text="Hexadecimal:").grid(row=2, column=0)
hex_entry = tk.Entry(root, textvariable=hex_result, width=50)
hex_entry.grid(row=2, column=1)
tk.Button(root, text="To Text & Binary", command=hex_to_text).grid(row=2, column=2)

root.mainloop()
