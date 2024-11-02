import webbrowser
import pyttsx3
from tkinter import *
from PIL import Image, ImageTk
import action
import spech_to_text


def speak_text(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()


def ask():
    try:
        ask_val = spech_to_text.spech_to_text()

        # Handle NoneType or empty input from speech recognition
        if ask_val is None or ask_val.strip() == "":
            text.insert(END, "Bot <-- I didn't catch that. Please try again.\n")
            return

        bot_val = action.Action(ask_val)
        text.insert(END, "Me --> " + ask_val + "\n")

        if bot_val is not None:
            text.insert(END, "Bot <-- " + str(bot_val) + "\n")

        if bot_val == "ok sir":
            root.destroy()

    except Exception as e:
        text.insert(END, "Bot <-- Error: " + str(e) + "\n")


def User_send():
    send = entry1.get()

    # Handle empty input from user
    if send.strip() == "":
        text.insert(END, "Bot <-- Please enter a message.\n")
        return

    bot = action.Action(send)
    text.insert(END, "My Message --> " + send + "\n")

    if bot is not None:
        text.insert(END, "AI Response <-- " + str(bot) + "\n")

    if bot == "ok sir":
        root.destroy()


def emergency():
    webbrowser.open("https://www.redcrossnigeria.org/")
    speak_text("Emergency services are being contacted.")
    return "Emergency services are being contacted. Please hold on."


def delete_text():
    text.delete("1.0", "end")


root = Tk()
root.geometry("550x675")
root.title("Computerized Personal Assistant")
root.resizable(False, False)
root.config(bg="#FFDAB9")

# Main Frame
Main_frame = LabelFrame(root, padx=100, pady=7, borderwidth=3, relief="raised", bg="purple")
Main_frame.grid(row=0, column=1, padx=55, pady=10)

# Text Label
Text_label = Label(Main_frame, text="Personal Assistant", font=("comic Sans ms", 14, "bold"))
Text_label.grid(row=0, column=0, padx=20, pady=10)

# Image
original_image = Image.open("image/user_male.jpg")
resized_image = original_image.resize((200, 200), Image.LANCZOS)
Display_Image = ImageTk.PhotoImage(resized_image)
Image_Label = Label(Main_frame, image=Display_Image)
Image_Label.grid(row=1, column=0, pady=20)

# Text widget
text = Text(root, font=('Courier 10 bold'), bg="purple", fg="white")
text.grid(row=2, column=0)
text.place(x=50, y=375, width=425, height=100)

# Entry widget
entry1 = Entry(root, justify=CENTER)
entry1.place(x=50, y=500, width=425, height=60)

# Buttons
button1 = Button(root, text="Speak", bg="purple", pady=15, padx=15, fg="white", borderwidth=2, relief="raised",
                 command=ask)
button1.place(x=10, y=75)

button2 = Button(root, text="Emergency", bg="purple", pady=15, padx=15, fg="white", borderwidth=2, relief="raised",
                 command=emergency)
button2.place(x=50, y=575)

button3 = Button(root, text="Send", bg="purple", pady=15, padx=15, fg="white", borderwidth=2, relief="raised",
                 command=User_send)
button3.place(x=400, y=575)

button4 = Button(root, text="Delete", bg="purple", pady=15, padx=15, fg="white", borderwidth=2, relief="raised",
                 command=delete_text)
button4.place(x=245, y=575)

root.mainloop()
