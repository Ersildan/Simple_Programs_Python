import random
from tkinter import *

def get_answer():
    otvet = Label(frame_bottom, text=random.choice(list_answers))


list_answers = [
                'Бесспорно', 'Мне кажется - да', 'Пока не ясно, попробуй снова', 'Даже не думай',
                'Предрешено', 'Вероятнее всего', 'Спроси позже', 'Мой ответ - нет', 'Никаких сомнений',
                'Хорошие перспективы', 'Лучше не рассказывать', 'По моим данным - нет', 'Определённо да',
                'Знаки говорят - да', 'Сейчас нельзя предсказать', 'Перспективы не очень хорошие',
                'Можешь быть уверен в этом', 'Да', 'Сконцентрируйся и спроси опять', 'Весьма сомнительно'
                ]

window = Tk()

window["bg"] = "#fafafa"
window.title("Шар Судьбы")
window.geometry('300x200')
window.resizable(width=False, height=False)

frame_top = Frame(window, bg='#ffb700', bd=5)
frame_top.place(relx=0.15, rely=0.15, relwidth=0.7, relheight=0.25)
frame_bottom = Frame(window, bg='#ffb700', bd=5)
frame_bottom.place(relx=0.15, rely=0.55, relwidth=0.7, relheight=0.1)

cityField = Entry(frame_top, bg='white', font=30)
cityField.pack()

btn = Button(frame_top, text='Узнать ответ', command=get_answer())
btn.pack()

info = Label(frame_bottom, text='Шар говорит:', bg='#ffb700', font=40)
info.pack()

window.mainloop()
