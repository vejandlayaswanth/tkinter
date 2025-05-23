import tkinter as tk
from tkinter import messagebox


root = tk.Tk()
root.title(" Greeting App")
root.geometry("600x260")
root.config(bg="lightblue")

def greet():
    name = enter_name.get()
    if name :
        messagebox.showinfo(f" Greetings",f"hello {name}! Welcome aboard 🎉 Learning is a journey, and every step you take brings you closer to something amazing. Keep going—you're doing great already! ")
    else:
        messagebox.showwarning(" Input error ","Please enter your name")
        
name = tk.Label(root, text = "Enter your name :")
name.pack(pady=26)

enter_name= tk.Entry(root)
enter_name.pack(pady=13)

button = tk.Button(root,text="Greet", command=greet)
button.pack(pady=13)

root.mainloop()