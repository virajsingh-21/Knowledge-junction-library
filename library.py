import tkinter as tk
import time

def start_animation():
    label1.config(text="Welcome to\nKnowledge Junction Library", font=("Arial", 24, "bold"), fg="blue")
    root.update()
    time.sleep(1)
    ask_question_1()

def ask_question_1():
    label2.config(text="Did you know about Knowledge Junction Library?", fg="black")
    btn_yes.config(command=yes_response_1)
    btn_no.config(command=no_response_1)
    btn_yes.pack(pady=5)
    btn_no.pack(pady=5)

def yes_response_1():
    label2.config(text="Wow! Wonderful ❤️", fg="green")
    root.update()
    time.sleep(1)
    ask_question_2()

def no_response_1():
    label2.config(text="Please search about it!", fg="red")
    root.update()
    time.sleep(1)
    ask_question_2()

def ask_question_2():
    label2.config(text="Kya aap is library me padhna chahte hain?", fg="black")
    btn_yes.config(command=yes_response_2)
    btn_no.config(command=no_response_2)
    btn_yes.pack(pady=5)
    btn_no.pack(pady=5)

def yes_response_2():
    label2.config(text="Congratulations and Welcome!", fg="blue")
    root.update()
    time.sleep(1)

def no_response_2():
    label2.config(text="Oh! Thanks for searching!", fg="purple")
    root.update()
    time.sleep(1)

# Window setup
root = tk.Tk()
root.title("Knowledge Junction Library")
root.geometry("500x400")
root.configure(bg="#ffffff")  # Background white

# Welcome label
label1 = tk.Label(root, text="", font=("Arial", 24), bg="#ffffff", fg="blue")
label1.pack(pady=20)

# Question label
label2 = tk.Label(root, text="", font=("Arial", 18), bg="#ffffff", fg="black")
label2.pack(pady=10)

# Yes and No buttons
btn_yes = tk.Button(root, text="Yes", font=("Arial", 14), bg="#0d47a1", fg="#ffffff")
btn_no = tk.Button(root, text="No", font=("Arial", 14), bg="#b71c1c", fg="#ffffff")

# Start Button
start_btn = tk.Button(root, text="Start", font=("Arial", 16), bg="#0d47a1", fg="#ffffff", command=start_animation)
start_btn.pack(pady=20)

# Start GUI loop
root.mainloop()