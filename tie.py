import tkinter as tk

def on_closing():
    root.destroy()

root = tk.Tk()
root.title("Test Window")
root.geometry("300x200")
label = tk.Label(root, text="Hello, Tkinter!")
label.pack(pady=20)
button = tk.Button(root, text="Close", command=on_closing)
button.pack(pady=10)
root.mainloop()