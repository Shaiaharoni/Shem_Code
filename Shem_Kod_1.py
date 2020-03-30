import random
import time
import tkinter as tk
from tkinter import messagebox


card_num=25
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

teams = ["Red", "Blue"]
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



def Check_answer():
    print(self)



# On-Game Functions:
def Print_board_by_attribute(att):  
    #GUI
    if att=="word":   
        for x in range(0,card_num):
            for x in range(0,card_num):
                Game_button(x)
            #b = tk.Button(word_window,text=words[x].word,height = 5, width = 10)
            #b.grid(column=x%5,row=30+int(x/5), padx=(10,10), pady=(10,10))
            
    else:
        color_window = Create_window()
        for x in range(0,card_num):
            b = tk.Button(color_window, bg=words[x].color,height = 5, width = 10)
            b.grid(column=x%5,row=int(x/5), padx=(5,5), pady=(5,5))
        color_window.mainloop()
    

def Find_index_by_word(word):
    words_list = list(map(lambda x: x.word, words))
    return words_list.index(word)


def Check_answers(answer):
    answer_index = Find_index_by_word(answer)
    if words[answer_index].color==teams[i]:
        return True
    else:
        return False

def Show_card_color(answer):
    index_to_flip = Find_index_by_word(answer)
    words[index_to_flip].word = words[index_to_flip].color

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

        
# Classes:
class Card:
  def __init__(self, word):
    self.word = word
    self.color = random.choice(card_types)
    card_types.remove(self.color)

class Game_button:
    def __init__(self, x):
        self.x=x
        self.word = words[x].word
        self.button = tk.Button(word_window,text=words[x].word,height = 5, width = 10, command=self.Get_word).grid(column=x%5,row=30+int(x/5), padx=(10,10), pady=(10,10))

    def Get_word(self):
        print(self.word)
        self.button = tk.Button(word_window,text="",height = 5, width = 10, command=self.Get_word, bg=words[self.x].color).grid(column=self.x%5,row=30+int(self.x/5), padx=(10,10), pady=(10,10))
        


############################## GAME ##############################
                            # Pre-Game
words = []
Init_game()

                            # On-Game

# Choose who start the game

i= 0 if red_appearance > blue_appearance else 1

while(win != True):
    word_window = Create_window()
    tk.Label(word_window, text=teams[i]+" team turn!").grid(row=0, column=2)
    tk.Label(word_window, text="Num of Cards:").grid(row=100, column=2)
    e1 = tk.Entry(word_window,textvariable=tk.StringVar(),width="10").grid(row=101, column=2)
    Print_board_by_attribute("word")
    word_window.update()
    
    #print("its", teams[i], "team turn!")
    #question = input("The Rav-Meraglim word is: ")
    #number_of_cards = int(input("number of cards:"))
    #Print_board_by_attribute("word")
    #for x in range(0,number_of_cards):
    #    answer = input()
    #    is_correct = Check_answers(answer)
    #    Show_card_color(answer)
    #    Print_board_by_attribute("word")
    #    if not is_correct:
    #        break

    win = Check_win()
    i = 1 - i

print("Game Over!")





