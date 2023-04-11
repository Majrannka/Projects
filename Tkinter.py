import tkinter as tk
from tkinter import ttk
from ctypes import windll
from random import randint

points = 0

root = tk.Tk()
root.title('Quiz Mnożenie')
root.geometry('600x400+50+50')

root.resizable(True, True)

ttk.Label(root, text="Witaj w grze Quiz Mnożenie!", font=("Ariel", 12)).pack()


def question_generator():
    task = ttk.Label(root, text="")

    first = randint(1, 10)
    second = randint(1, 10)
    question = "Jaki jest wynik " + str(first) + "*" + str(second) + "?"
    task["text"] = question
    task.pack()

    text = tk.StringVar()
    answer = ttk.Entry(root, textvariable=text)
    answer.pack()

    check = ttk.Button(root, text="Zatwierdź", command=lambda: check_clicked(check, text, first, second))
    check.pack()


def check_clicked(button, ans, a, b):
    disable(button)
    check_answer(ans, a, b)


def disable(button):
    button["state"] = tk.DISABLED


def check_answer(ans, a, b):
    global points

    if ans.get() == str(a * b):
        points += 1
        pnt = str(points)
        com1 = "Poprawna odpowiedź! Liczba punktów: " + pnt
        communicate = ttk.Label(root, text=com1)
    else:
        pnt = str(points)
        com = "Źle! Poprawna odpowiedź to: " + str(a*b) + ". Liczba punktów: " + pnt
        communicate = ttk.Label(root, text=com)

    communicate.pack()


def finish_game():
    new_question["state"] = tk.DISABLED

    pnt = str(points)
    final_communicate = "Dziękuję za grę! Liczba zdobytych punktów: " + pnt
    final = ttk.Label(root, text=final_communicate)
    final.pack()


new_question = ttk.Button(root, text='Nowe pytanie', command=question_generator)
new_question.pack()
finish = ttk.Button(root, text='Zakończ', command=finish_game)
finish.pack()

try:
    windll.shcore.SetProcessDpiAwareness(1)
finally:
    root.mainloop()
