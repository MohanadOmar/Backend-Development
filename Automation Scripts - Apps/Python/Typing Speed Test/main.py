import random
import tkinter as tk
from tkinter import *
from datetime import datetime

win = tk.Tk()
win.title("Speed Typing Test")

# Welcome Text
welcome_text = tk.Label(win, text="Press start to begin :)\n")
welcome_text.grid(row=0, column=0, columnspan=3)


def clear_frame():
    for widgets in win.winfo_children():
        if widgets == welcome_text or widgets == start_button:
            pass
        else:
            widgets.destroy()


def start():
    clear_frame()
    start_time = datetime.now().strftime("%M %S").split(" ")
    start_time_sec = (int(start_time[0]) * 60) + int(start_time[1])
    print(start_time_sec)

    # Choosing random sentence
    all_sentences = ["i am mohanad omar",
                     "still hustling to find dollars for the quarter end.",
                     "doug chapman will likely get the start in bennett s absence.",
                     "the senate would require them to create a us subsidiary."]
    random_sentence = random.choice(all_sentences)
    # Displaying the sentence
    sentence = tk.Label(win, text=random_sentence.title())
    sentence.grid(row=1, column=1)

    num_of_words_in_sentence = len(random_sentence.split(" "))

    def callback(event):
        text = event.widget.get()
        if text == random_sentence:
            print("Done")
            end_time = datetime.now().strftime("%M %S").split(" ")
            end_time_sec = (int(end_time[0]) * 60) + int(end_time[1])
            print(end_time_sec)

            time_taken = (end_time_sec - start_time_sec) / 60

            speed = round(num_of_words_in_sentence / time_taken)
            speed_label = tk.Label(win, text=f"{speed} words/min")
            speed_label.grid(row=2, column=1)

    # Making the entry
    m = StringVar()
    test_entry = tk.Entry(win, width=120, textvariable=m)
    test_entry.bind('<KeyPress-Return>', callback)
    test_entry.grid(row=3, columnspan=3)
    message = Message(win, textvariable=m)


# Start Button
start_button = tk.Button(win, text="Start", width=50, command=start)
start_button.grid(row=4, column=1)

win.mainloop()
