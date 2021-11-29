from tkinter import *
from random import randint
from time import sleep
#Creating the window
window=Tk()
window.title('Snake')
c=Canvas(window, width=255, height=255, bg='black')
c.pack()
#snake stuff
snake_parts = list()
sp_1 = c.create_rectangle(115, 115, 125, 125, fill='white')
snake_parts.append(sp_1)
s_dir = list()
s_dir.append(2)
#making the apple and getting coordinates
apple = list()
def grow_apple(food):
    if food == 0:
            y=randint(1, 25)*10
            x=randint(1, 25)*10
            aple=c.create_rectangle(x-5, y-5, x+5, y+5, fill='red')
            apple.append(aple)
            ap_nsp = 1
            while ap_nsp == 1:
                x1, y1 = get_coords(apple[0])
                for  i in range(len(snake_parts)):
                    x2, y2 = get_coords(snake_parts[i])
                    if x1 == x2:
                        if y1 == y2:
                            c.delete(apple[0])
                            y=randint(1, 25)*10
                            x=randint(1, 25)*10
                            aple=c.create_rectangle(x-5, y-5, x+5, y+5, fill='red')
                            apple[0] = aple
                            ap_nsp = 1
                            break
                        else:
                            ap_nsp = 0
                    else:
                        ap_nsp = 0
            return 1
def get_coords(id_num):
    pos=c.coords(id_num)
    x=(pos[0] + pos[2])/2
    y=(pos[1] + pos[3])/2
    return x, y
#Turn/Move/Grow snake
def grow_snake(food):
    if food == 0 :
        x, y =get_coords(snake_parts[len(snake_parts) - 1])
        if s_dir[len(snake_parts) - 1] == 1 :
            y += 10
        elif s_dir[len(snake_parts) - 1] == 2 :
            x -= 10
        elif s_dir[len(snake_parts) - 1] == 3 :
            y -= 10
        else :
            x += 10
        sp_2 = c.create_rectangle(x-5, y-5, x+5, y+5, fill='white')
        snake_parts.append(sp_2)
        s_dir.append(s_dir[len(snake_parts) - 2])
def move_snake():
    if len(s_dir) >= 2:
        if s_dir[0] + 2 == s_dir[1]:
            s_dir[0] = s_dir[1]
        elif s_dir[0] - 2 == s_dir[1]:
            s_dir[0] = s_dir[1]
    for i in range(len(snake_parts)):
        if s_dir[i] == 1 :
            c.move(snake_parts[i], 0, -10)
        elif s_dir[i] == 2 :
            c.move(snake_parts[i], 10, 0)
        elif s_dir[i] == 3 :
            c.move(snake_parts[i], 0, 10)
        elif s_dir[i] == 4 :
            c.move(snake_parts[i], -10, 0)
    for i in reversed(range(len(snake_parts))):
        if i > 0 :
            s_dir[i] = s_dir[i-1]
def turn_snake(event):
    if event.keysym == 'Up':
        del s_dir[0]
        s_dir.insert(0, 1)
    if event.keysym == 'Right':
        del s_dir[0]
        s_dir.insert(0, 2)
    if event.keysym == 'Down':
        del s_dir[0]
        s_dir.insert(0, 3)
    if event.keysym == 'Left':
        del s_dir[0]
        s_dir.insert(0, 4)
c.bind_all('<Key>', turn_snake)
#Colision detection and eating apple
def hitting_wall():
    x, y = get_coords(snake_parts[0])
    if x == 260 :
        return True
    elif x == 0 :
        return True
    elif y == 260 :
        return True
    elif y == 0 :
        return True
    else :
        return False
def hitting_tail():
    for i in range(len(snake_parts)-2):
        i += 2
        x1, y1 = get_coords(snake_parts[0])
        x2, y2 = get_coords(snake_parts[i])
        if x1 == x2 :
            if y1 == y2 :
                return True
    return False
def eating_apple(food, a, score):
    x1, y1 = get_coords(snake_parts[0])
    x2, y2 = get_coords(apple[0])
    if x1 == x2 :
        if y1 == y2 :
            food = 0
            c.delete(apple[0])
            del apple[0]
            score += 1
            if a >= 0.01:
                a -= 0.001
    return food, a, score
#Main game loop and endgame
food = 0
a=0.1
score = 0
while True:
    food = grow_apple(food)
    move_snake()
    food, a, score = eating_apple(food, a, score)
    grow_snake(food)
    if hitting_wall() :
        break
    if hitting_tail() :
        break
    window.update()
    sleep(a)
c.create_text(125, 125, text='GAME OVER', fill='white', font=('Helvetica',30))
c.create_text(125, 155, text='Score: '+ str(score), fill='white')
