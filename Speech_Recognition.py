import tkinter as tk
import speech_recognition as sr
from tkinter import ttk
from tkinter import *

r = sr.Recognizer()

# Use the 'clam' theme for the window



def start_listening():
    T.delete("1.0","end")
    global mic
    mic = sr.Microphone()
    with mic as source:
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)

    try:
        text = "You Said : "+r.recognize_google(audio)
        T.insert(END, text + "\n")
    except sr.UnknownValueError:
        T.insert(END, "Could not understand audio\n")
    except sr.RequestError as e:
        T.insert(END, "Error: " + str(e) + "\n")
    except Exception as e:
        T.insert(END, "Error: " + str(e) + "\n")
    count =+ 1
        
main = tk.Tk()
main.title("AI-GUI")
main.geometry("1080x720")
main.resizable(width=FALSE, height=FALSE)
main.configure(background="#333333")

T = Text(main, height=5, width=52,borderwidth=3)
T.configure(background="#D3D3D3",bd=0)
T.place(x=60, y=400, width=960, height=250)
T.insert(INSERT,"\n\n\n                                      Click on record for starting speech to text.                                      \n\n                                            To clear text click on Clear.                                            \n\n                                     Whatever you speak the text of it appears here                                    ")

#click_btn = PhotoImage(file='download.png')
label = tk.Label(main, text="Press the button to record the Audio", font=(200))
label.configure(background="#333333",foreground="white")
label.place(x=390, y=170)

def about():
    T.delete("1.0","end")
    T.insert(INSERT,"------------------------------------------------------------------------------------------------------------------\n")
    T.insert(INSERT,"About Speech Recognizer: \n")
    T.insert(INSERT,"This program will convert the speech of the user to the text format..\n")
    T.insert(INSERT,"------------------------------------------------------------------------------------------------------------------\n")
    T.insert(INSERT,"Welcome to our community of tech enthusiasts! We're passionate about helping you expand your knowledge and skills in various areas of technology. Whether you're a beginner or an experienced professional, we offer a variety of resources and events to help you stay up-to-date with the latest trends and developments in your field. Join us to connect with like-minded individuals, collaborate on projects, and share your knowledge and skills with others. We're committed to providing a supportive and inclusive environment for everyone who wants to learn and grow. Let's explore the exciting world of technology together!")

def clear():
    T.delete("1.0", "end")

about_button = Button(main,text="ABOUT",relief="flat",highlightthickness=0,activeforeground="White",
                      command=about,background="#D3D3D3",foreground="black", activebackground="black")
about_button.place(x=60,y=10)
about_button.configure(width=136)

canvas = tk.Canvas(main, width=50, height=50, highlightthickness=0,background="#333333")
canvas.create_oval(0, 0, 50, 50, fill='black')
rec_button = Button(main,text="RECORD", relief="flat", highlightthickness=0, bd=0,width=6,activeforeground="cyan",activebackground="black",background="black",foreground="white",command=start_listening)

# Position the button inside the canvas
canvas.create_window(25, 25, window=rec_button)
canvas.place(x=500,y=225)

clear_button = Button(main,text="CLEAR",relief="flat",highlightthickness=0,activeforeground="White",
                      command=clear,background="#333333",foreground="white", activebackground="black")
clear_button.place(x=560,y=238)



main.mainloop()
