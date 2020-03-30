import random
import time
import tkinter as tk
from tkinter import messagebox


card_num = 25
txt_file_dir = 'C:\\Users\\97252\\Desktop\\Shem_Kod\\words.txt'
card_types = []
appearances = [8,9]
red_appearance = random.choice(appearances)
appearances.remove(red_appearance)
blue_appearance = appearances[0]
 

card_types += red_appearance * ["Red"]
card_types += blue_appearance * ["Blue"]
card_types += 7 * ["White"]
card_types += ["Black"]
i = 0 if red_appearance > blue_appearance else 1
teams = ["Red", "Blue"]


# Classes:
class Card:
  def __init__(self, word):
    self.word = word
    self.color = random.choice(card_types)
    card_types.remove(self.color)



class Turn:
    def __init__(self, i):
        self.i = i 
        self.turn_string = tk.Label(word_window, text=teams[self.i] + " team turn!").grid(row=0, column=2)
    
    def Change_team(self):
        self.i = 1 - self.i
        self.turn_string = tk.Label(word_window, text=teams[self.i] + " team turn!").grid(row=0, column=2)

class Game_button:
    def __init__(self, x):
        self.x = x
        self.word = words[x].word
        self.button = tk.Button(word_window,text=words[x].word,height = 5, width = 10, command=self.Get_word).grid(column=x % 5,row=30 + int(x / 5), padx=(10,10), pady=(10,10))

    def Get_word(self):
        self.button = tk.Button(word_window,text="",height = 5, width = 10, bg=words[self.x].color).grid(column=self.x % 5,row=30 + int(self.x / 5), padx=(10,10), pady=(10,10))
        if Check_answers(self.word):
            turn.Change_team()


win = False


# Pre-Game Functions:
def Get_words():
    txt_words = open(txt_file_dir, 'r', encoding="utf8").readlines()
    chosen_words = random.choices(txt_words,k=25)
    for word in chosen_words:
        words.append(Card(word[:-1]))

def Create_window():
    window = tk.Tk()
    window.configure(background='#003366')
    window.title("Shem Kod")
    return window

def Init_game():
    print("It's SHEM-KOD GAME!")
    Get_words()
    Print_board_by_attribute("color")



# On-Game Functions:
def Print_board_by_attribute(att):  
    #GUI
    if att == "word":   
        for x in range(0,card_num):
            for x in range(0,card_num):
                Game_button(x)
    else:
        color_window = Create_window()
        for x in range(0,card_num):
            b = tk.Button(color_window, bg=words[x].color,height = 5, width = 10)
            b.grid(column=x % 5,row=int(x / 5), padx=(5,5), pady=(5,5))
        color_window.mainloop()
    

def Find_index_by_word(word):
    words_list = list(map(lambda x: x.word, words))
    return words_list.index(word)


def Check_answers(answer):
    answer_index = Find_index_by_word(answer)
    if words[answer_index].color == teams[turn.i]:
        return True
    else:
        return False

#def Show_card_color(answer):
#    index_to_flip = Find_index_by_word(answer)
#    words[index_to_flip].word = words[index_to_flip].color

def Check_win():
    w = list(map(lambda x: x.word, words))
    if w.count("Red") == red_appearance:
        print("Red Team won")
        return True
    elif w.count("Blue") == blue_appearance:
        print("Blue Team won")
        return True
    elif w.count("Black") == 1:
        return True
    else:
        return False

        



############################## GAME ##############################
                            # Pre-Game
words = []
Init_game()

                            # On-Game

word_window = Create_window()
turn = Turn(i)
tk.Label(word_window, text="Num of Cards:").grid(row=100, column=2)
e1 = tk.Entry(word_window,textvariable=tk.StringVar(),width="10").grid(row=101, column=2)
Print_board_by_attribute("word")
    
win = Check_win()
word_window.mainloop()

print("Game Over!")





