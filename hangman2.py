import random
#from random_word import RandomWords
from tkinter import *
#from PIL import ImageTk
import tkinter as t
import time

#words = RandomWords()
window = t.Tk()
window.geometry('1000x750')
window.configure(background='orange')
greeting = Label(window, text = 'Hangman', bg='orange', fg='blue', font=(None, 70))
greeting.place(x=50, y=10)
#how to get them to disappear

hangs = [t.PhotoImage(file='hang1.png'), t.PhotoImage(file='hang2.png'), t.PhotoImage(file='hang3.png'),
 t.PhotoImage(file='hang4.png'), t.PhotoImage(file='hang5.png'), t.PhotoImage(file='hang6.png'),
t.PhotoImage(file='hang7.png')]

the_word = random.choice(['pick', 'shovel', 'djambok', 'jail', 'journey', 'wield',
'chaos', 'halo', 'infinite', 'woe', 'gravel', 'luxury', 'dwell']).upper() #get an actual dictionary
lst_word = []
for i in the_word:
    lst_word.append(i)

length = len(the_word)
repr = ''
for i in range(length):
    repr += '_ '
#repr = ' '.join(repr)
lst_repr = []
for x in range(length):
    lst_repr.append('_')
    #lst_repr.append(' ')
initial = t.Label(window , text = repr, bg='orange', fg='black', font=(None, 45))
#initial.pack()
initial.place(x=300, y=350)
start_wrong = t.Label(window, text = 'Incorrect: 0', bg='orange', fg='black', font=(None, 30))
#start_wrong,pack()
start_wrong.place(x=300, y=230)

total_guesses = 10
wrongs = 0
new_lst = lst_repr
entering = Label(window, text = 'Guess a letter! ', bg='orange', fg='black', font=(None, 30))
entering.place(x=400, y=400)
entering.pack()
n = Entry()
time.sleep(1)
n.pack()

hang_start = t.Label(window, image=hangs[0])
hang_start.place(x=650, y=150)
#hangs.grid(row=0, column=0, columnspan=2, padx=700, pady=180)
#hangs.config(image=hangs[0])

def evaluating():
    global total_guesses
    global wrongs
    global lst_word
    global new_lst
    global let_repr
    global repr
    new = n.get()
    #hangs.config(image=hangs[0])
    if total_guesses > 0:
        #new = n.get()
        #condiiton for when input is not a letter
        if new.upper() not in the_word.upper():
            wrongs += 1
            if wrongs == 6:
                final = t.Label(window, text = 'Game over! The word was ' + the_word + '!', bg='orange', fg='red', font=(None, 50))
                final.place(x=100, y=550)
            new_wrong = t.Label(window, text = 'Incorrect: ' + str(wrongs), bg='orange', fg='black', font=(None, 30))
            new_wrong.place(x=300, y=230)
            hang_now = t.Label(window, image=hangs[wrongs])
            hang_now.place(x=650, y=156)
            #hangs.grid(row=0, column=0, columnspan=2, padx=700, pady=180)
            #hangs.config(image=hangs[wrongs])
            #window.set(wrongs)
            #insert hangman image
        else:
            for i in range(len(lst_word)):
                if lst_word[i] == new.upper():
                    lst_repr[i] = lst_word[i]
        updated_word = ''
        for j in lst_repr:
            updated_word += j
        new_lst = lst_repr
        word_now = t.Label(window, text = new_lst, bg='orange', fg='black', font=(None, 45))
        word_now.place(x=300, y=350)
        if updated_word == the_word:
            win = t.Label(window, text = 'You guessed the word! Well done!', bg='orange', fg='green', font=(None, 50))
            win.place(x=100, y=550)
        total_guesses -= 1
    #else:
        #if updated_word == the_word:

    #n.delete(0, t.END)
#while new_lst != the_word:
    #evaluating()
#hangs = Label(window)
#hangs.grid(row=0, column=0, columnspan=2, padx=700, pady=180)
#hangs.config(image=hangs[0])

button = Button(window, text = 'Submit', width = 15, command = evaluating)
button.pack()

mainloop()
