from tkinter import *
import random
from tkinter import ttk


root = Tk()
root.geometry('700x700')
root.title('Nickname Generator')
root.resizable(False, False)


first_word = ["Brave", "Smart", "Bold", "Fierce", "Loyal", "Valiant", "Fearless", "Swift",
    "Mystic", "Mighty", "Stealthy", "Silent", "Reckless", "Savage", "Phantom",
    "Stormy", "Wild", "Rogue", "Shadow", "Daring", "Cunning", "Sniper", "Warrior",
    "Epic", "Grim", "Vivid", "Lucky", "Crazy", "Relentless", "Fear", "Titan", 
    "Agile", "Sharp", "Venomo"]

second_word = [  "Warrior", "Rebel", "Titan", "Phantom", "Shadow", "Rogue", "Sniper", "Hunter",
    "Hero", "Titan", "Hunter", "Rogue", "Rebel", "Warrior", "Sniper", "Titan",
    "Phantom", "Shadow", "Hero", "Sniper", "Titan", "Phantom", "Shadow", "Rebel",
    "Warrior", "Sniper", "Phantom", "Rogue", "Hunter", "Phantom", "Shadow", "Rebel",
    "Titan", "Phantom", "Hunter", "Warrior", "Rogue", "Shadow", "Rebel", "Warrior",
    "Phantom", "Sniper", "Rogue"]



def gen():
    nickname = random.choice(first_word) + random.choice(second_word)
    return nickname

label_style = ttk.Style()
label_style.configure("My.TLabel",          # имя стиля
                    font="helvetica 19",    # шрифт
                    foreground="#FFFFCC",   # цвет текста
                    padding=10,             # отступы
                    background="#000000")   # фоновый цвет
 


main_label = ttk.Label(text="Random Nickname Generator",anchor="center", style="My.TLabel")
main_label.place(x=20, y=30, width=660) # приветственная плашка

#   добавить выбор тольео одно слово или два слова для никнейма
#   добавить вывод результата, кнопку копировать
#    добавиь кнопку Сгенерировать
#
root.mainloop()