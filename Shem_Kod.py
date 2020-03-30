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

#def Insert_words():
#    print("Enter", card_num, "words:")
#    for i in range(0,card_num):
#        words.append(Card(input()))

#def Clear_terminal():
#        print("\n"*40)

def Init_game():
    print("It's SHEM-KOD GAME!")
    Get_words()
#    Insert_words()
    Print_board_by_attribute("color")
#    Clear_terminal()


# On-Game Functions:
def Print_board_by_attribute(att):
#    print()
#    if att=="color":
#        wait = input("turn around - only RAVE-MERAGLIM can look! \npress ENTER to continue!")
#        print()
#    for x in range(0,card_num, 5):
#        print(getattr(words[x],att),"|",
#              getattr(words[x+1],att),"|",
#             getattr(words[x+2],att),"|",
#              getattr(words[x+3],att),"|",
#              getattr(words[x+4],att))
#    if att=="color":
#        print()
#        wait=input("Take an image with your phone! \npress Enter to continue!")
#    print()

    

    #GUI
    if att=="word":
        
        
        for x in range(0,card_num):
            Game_button(tk.Button(word_window,text=words[x].word,height = 5, width = 10).grid(column=x%5,row=30+int(x/5), padx=(10,10), pady=(10,10)))
            #b = tk.Button(word_window,text=words[x].word,height = 5, width = 10)
            #b.grid(column=x%5,row=30+int(x/5), padx=(10,10), pady=(10,10))
        
    else:
        #window configuration
        color_window = tk.Tk()
        color_window.configure(background='#003366')
        for x in range(0,card_num):
            b = tk.Button(color_window, bg=words[x].color,height = 5, width = 10)
            b.grid(column=x%5,row=int(x/5), padx=(10,10), pady=(10,10))
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
    def __init__(self, button):
        self.button = button

############################## GAME ##############################
                            # Pre-Game
words = []
Init_game()

                            # On-Game
# Choose who start the game

i= 0 if red_appearance > blue_appearance else 1

while(win != True):
    #Clear_terminal()
    word_window = tk.Tk()
    
    word_window.configure(background='#003366')
    word_window.title("Shem Kod")
    Print_board_by_attribute("word")
    messagebox.showinfo("Information","its " + teams[i] + " team turn!")
    word_window.mainloop()
    
    print("its", teams[i], "team turn!")
    question = input("The Rav-Meraglim word is: ")
    number_of_cards = int(input("number of cards:"))
    Print_board_by_attribute("word")
    for x in range(0,number_of_cards):
        answer = input()
        is_correct = Check_answers(answer)
        Show_card_color(answer)
        Print_board_by_attribute("word")
        if not is_correct:
            break

    win = Check_win()
    i = 1 - i

print("Game Over!")





