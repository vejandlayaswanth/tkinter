import tkinter as tk

root = tk.Tk()
root.title("My First GUI")
root.geometry("400x300")

def hello():
    print("hello  , this is your first tkinter program")
    
hello_button = tk.Button(root, text="Click Me", command=hello)
hello_button.pack(pady=20)
root.mainloop()