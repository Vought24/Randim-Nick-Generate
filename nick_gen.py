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



one_word_choice = 'Simple nickname(one word)'
two_word_choice = 'Advanced nickname'

default_choice = StringVar(value=two_word_choice)

nickname_simple = random.choice(second_word)
nickname_advanced = random.choice(first_word) + random.choice(second_word)


label_style = ttk.Style()
label_style.configure("My.TLabel",          # имя стиля
                    font="helvetica 19",    # шрифт
                    foreground="#FFFFCC",   # цвет текста
                    padding=10,             # отступы
                    background="#000000")   # фоновый цвет
 


main_label = ttk.Label(text="Random Nickname Generator",anchor="center", style="My.TLabel")
main_label.place(x=20, y=30, width=660) # приветственная плашка

#   добавить выбор тольео одно слово или два слова для никнейма
choice_one = ttk.Radiobutton(text=one_word_choice, cursor='hand2', value=one_word_choice, variable=default_choice, )
choice_one.place(x=50, y=200)
choice_advanced = ttk.Radiobutton(text=two_word_choice, cursor='hand2', value=two_word_choice, variable=default_choice)
choice_advanced.place(x=400, y=200)

def gen():
    if default_choice.get() == one_word_choice:
        nickname_simple = random.choice(second_word)
        result_entry.delete(0, END)  
        result_entry.insert(0, nickname_simple)
    elif default_choice.get() == two_word_choice:
        nickname_advanced = random.choice(first_word) + "_" + random.choice(second_word)
        result_entry.delete(0, END) 
        result_entry.insert(0, nickname_advanced)

# Generate button
btn_gen = ttk.Button(text='Generate!', command=gen, cursor='hand2')
btn_gen.place(x=250, y=250)

# Result display field
result_entry = ttk.Entry(font=("Helvetica", 14), width=30)
result_entry.place(x=200, y=300)
#
root.mainloop()
