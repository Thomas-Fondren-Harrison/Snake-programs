from tkinter import *
from random import randint
from time import sleep
#Creating the window
height=505
width=505
window=Tk()
window.title('Snake')
c=Canvas(window, width=width, height=height, bg='black')
c.pack()
#snake stuff
snake_parts = list()
sp_1 = c.create_rectangle(120 - 5, 250 - 5, 120 + 5, 250 + 5, fill='white')
snake_parts.append(sp_1)
s_dir = list()
s_dir.append(2)
#making the apple and getting coordinates
apple = list()
def grow_apple(food):
    if food == 0:
        y=randint(1, 50)*10
        x=randint(1, 50)*10
        aple=c.create_rectangle(x-5, y-5, x+5, y+5, fill='red')
        apple.append(aple)
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
turns = [[38, 1], [24, 4], [49, 3], [1, 2], [48, 3], [1, 4], [48, 3], [1, 2], [48, 3], [1, 4], [48, 3], [1, 2], [48, 3], [1, 4], [48, 3], [1, 2], [48, 3], [1, 4], [48, 3], [1, 2], [48, 3], [1, 4], [48, 3], [1, 2], [48, 3], [1, 4], [48, 3], [1, 2], [48, 3], [1, 4], [48, 3], [1, 2], [48, 3], [1, 4], [48, 3], [1, 2], [48, 3], [1, 4], [48, 3], [1, 2], [48, 3], [1, 4], [48, 3], [1, 2], [48, 3], [1, 4], [48, 3], [1, 2], [48, 3], [1, 4], [48, 3], [1, 2], [48, 3], [1, 4], [48, 3], [1, 2], [48, 3], [1, 4], [48, 3], [1, 2], [48, 3], [1, 4], [48, 3], [1, 2], [48, 3], [1, 4], [48, 3], [1, 2], [48, 3], [1, 4], [48, 3], [1, 2], [48, 3], [1, 4], [48, 3], [1, 2], [48, 3], [1, 4], [48, 3], [1, 2], [48, 3], [1, 4], [48, 3], [1, 2], [48, 3], [1, 4], [48, 3], [1, 2], [48, 3], [1, 4], [48, 3], [1, 2], [48, 3], [1, 4], [48, 3], [1, 2], [48, 3], [1, 4], [48, 3], [1, 2], [49, 1], [25, 1], [1, 1]]
def turn_snake(t, d, e):
    x1, y1 = get_coords(apple[0])
    x2, y2 = get_coords(snake_parts[0])
    if x1 != x2:
        if x1 + 10 != x2:
            if t == 0:
                d += 1
    if t == turns[d][0]:
        del s_dir[0]
        s_dir.insert(0, turns[d][1])
        t = 0
        d += 1
    if d == (len(turns) - 1):
        d = 0
        if e == 1 :
            del turns[0]
            e = 0
    return t, d, e
#Colision detection and eating apple
def hitting_wall():
    x, y = get_coords(snake_parts[0])
    if x == 510 :
        return True
    elif x == -10 :
        return True
    elif y == 510 :
        return True
    elif y == -10 :
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
def eating_apple(food):
    x1, y1 = get_coords(snake_parts[0])
    x2, y2 = get_coords(apple[0])
    if x1 == x2 :
        if y1 == y2 :
            food = 0
            c.delete(apple[0])
            del apple[0]
    return food
#Main game loop and endgame
food = 0
t = 0
d = 0
e = 1
while True:
    food = grow_apple(food)
    t, d, e = turn_snake(t, d, e)
    move_snake()
    food = eating_apple(food)
    grow_snake(food)
    end = hitting_wall()
    if end :
        break
    end = hitting_tail()
    if end :
        break
    window.update()
    sleep(0.01)
    t +=  1
c.create_text(250, 250, \
    text='GAME OVER', fill='white', font=('Helvetica',30))

