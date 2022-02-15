# Вы когда-нибудь играли в игру "Крестики-нолики"? Попробуйте создать её.from tkinter import *
from curses import window
from tkinter import *
import random
import tkinter.messagebox as mb

window = Tk()
window.geometry("340x295+500+250")
window.title('Крестики ноилки')
window.resizable(False, False)
game_run = True
game_place = []
cross_count = 0
        
def new_game():
    for row in range(3):
        for col in range(3):
            game_place[row][col]['text'] = ' '
    global game_run
    global cross_count
    game_run = True
    cross_count = 0

def move(row, col):
    if game_run and game_place[row][col]['text'] == ' ':
        game_place[row][col]['text'] = 'X'
        global cross_count 
        cross_count += 1
        check_win('X')
        if game_run and cross_count < 5:
            comp_move()
            check_win('O')
        if game_run and cross_count == 5:
            mb.showinfo("", "Ничья")
            
def check_line(a, b, c, char):
    if a['text'] == char and b['text'] == char and c['text'] == char:
        global game_run
        game_run = False
        if char == 'O':
            mb.showinfo("", "Ты проиграл(((")
        else:
            mb.showinfo("", "Ты выйграл!!!")

def check_win(char):
    for i in range(3):
        check_line(game_place[i][0], game_place[i][1], game_place[i][2], char)
        check_line(game_place[0][i], game_place[1][i], game_place[2][i], char)
    check_line(game_place[0][0], game_place[1][1], game_place[2][2], char)
    check_line(game_place[0][2], game_place[1][1], game_place[2][0], char)
    
def can_win(a, b, c, char):
    result = False
    if a['text'] == char and b['text'] == char and c['text'] == ' ':
        c['text'] = 'O'
        result = True
    if a['text'] == char and b['text'] == ' ' and c['text'] == char:
        b['text'] = 'O'
        result = True
    if a['text'] == ' ' and b['text'] == char and c['text'] == char:
        a['text'] = 'O'
        result = True
    return result

def comp_move():
    for i in range(3):
        if can_win(game_place[i][0], game_place[i][1], game_place[i][2], 'O'):
            return
        if can_win(game_place[0][i], game_place[1][i], game_place[2][i], 'O'):
            return
    if can_win(game_place[0][0], game_place[1][1], game_place[2][2], 'O'):
        return
    if can_win(game_place[0][2], game_place[1][1], game_place[2][0], 'O'):
        return
    for i in range(3):
        if can_win(game_place[i][0], game_place[i][1], game_place[i][2], 'X'):
            return
        if can_win(game_place[0][i], game_place[1][i], game_place[2][i], 'X'):
            return
    if can_win(game_place[0][0], game_place[1][1], game_place[2][2], 'X'):
        return
    if can_win(game_place[0][2], game_place[1][1], game_place[2][0], 'X'):
        return
    while True:
        row = random.randint(0, 2)
        col = random.randint(0, 2)
        if game_place[row][col]['text'] == ' ':
            game_place[row][col]['text'] = 'O'
            break
        
for row in range(3):
    line = []
    for col in range(3):
        button = Button(window, text = ' ', width=7, height=3, 
                        font=("Times New Roman", 21, "bold"), 
                        command = lambda row=row, col=col: move(row, col))
        button.grid(row=row, column=col)
        line.append(button)
    game_place.append(line)
new_game_button = Button(window, text='Новая игра', command=new_game)
new_game_button.grid(row=3, column=0, columnspan=3, sticky='senw')
    
    
window.mainloop()
    

