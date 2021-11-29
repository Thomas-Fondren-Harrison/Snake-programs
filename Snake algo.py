from tkinter import *
from random import randint
from time import sleep
#Creating the window
window=Tk()
window.title('Snake')
c=Canvas(window, width=255, height=255, bg='black')
c.pack()
#snake stuff
scores=list()
r = 1
d = 0
wall = 0
tail = 0
s_game = input('Show averages > ')
s_ro = input('Show rounds > ')
sleeps = input('Sleep > ')
for i in range(int(input('Rounds > '))):
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
            x, y = get_coords(snake_parts[len(snake_parts) - 1])
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
    def turn_snake():
        x1, y1 = get_coords(apple[0])
        x2, y2 = get_coords(snake_parts[0])
        if x1 > x2:
            if s_dir[0] == 4:
                if y1 > y2:
                    del s_dir[0]
                    s_dir.insert(0, 3)
                elif y2 > y1:
                    del s_dir[0]
                    s_dir.insert(0, 1)
                elif x2 > x1:
                    del s_dir[0]
                    s_dir.insert(0, 2)
                else:
                    del s_dir[0]
                    s_dir.insert(0, (randint(0,1)*2+1))
            else :
                del s_dir[0]
                s_dir.insert(0, 2)
        elif x1 < x2:
            if s_dir[0] == 2:
                if y1 > y2:
                    del s_dir[0]
                    s_dir.insert(0, 3)
                elif y2 > y1:
                    del s_dir[0]
                    s_dir.insert(0, 1)
                elif x2 < x1:
                    del s_dir[0]
                    s_dir.insert(0, 4)
                else:
                    del s_dir[0]
                    s_dir.insert(0, (randint(0,1)*2+1))
            else:
                del s_dir[0]
                s_dir.insert(0, 4)
        elif y1 > y2:
            if s_dir[0] == 1:
                if x1 > x2:
                    del s_dir[0]
                    s_dir.insert(0, 2)
                elif x2 > x1:
                    del s_dir[0]
                    s_dir.insert(0, 4)
                elif y2 > y1:
                    del s_dir[0]
                    s_dir.insert(0, 3)
                else:
                    del s_dir[0]
                    s_dir.insert(0, (randint(1,2)*2))
            else:
                del s_dir[0]
                s_dir.insert(0, 3)
        elif y1 < y2:
            if s_dir[0] == 3:
                if x1 > x2:
                    del s_dir[0]
                    s_dir.insert(0, 2)
                elif x2 > x1:
                    del s_dir[0]
                    s_dir.insert(0, 4)
                elif y2 < y1:
                    del s_dir[0]
                    s_dir.insert(0, 1)
                else:
                    del s_dir[0]
                    s_dir.insert(0, (randint(1,2)*2))
            else:
                del s_dir[0]
                s_dir.insert(0, 1)
        for i in range(len(snake_parts)):
            if i > 2:
                x3, y3 = get_coords(snake_parts[i])
                if x3 + 10 == x2:
                    if y2 == y3:
                        if s_dir[0] == 4:
                            for a in range(len(s_dir)):
                                if s_dir[i] != s_dir[0]:
                                    s_dir[0] = s_dir[i]
                                    break
                elif x3 - 10 == x2:
                    if y2 == y3:
                        if s_dir[0] == 2:
                            for a in range(len(s_dir)):
                                if s_dir[i] != s_dir[0]:
                                    s_dir[0] = s_dir[i]
                                    break
                elif y3 + 10 == y2:
                    if x2 == x3:
                        if s_dir[0] == 1:
                            for a in range(len(s_dir)):
                                if s_dir[i] != s_dir[0]:
                                    s_dir[0] = s_dir[i]
                                    break
                elif y3 + 10 == y2:
                    if x2 == x3:
                        if s_dir[0] == 3:
                            for a in range(len(s_dir)):
                                if s_dir[i] != s_dir[0]:
                                    s_dir[0] = s_dir[i]
                                    break
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
        turn_snake()
        move_snake()
        food, a, score = eating_apple(food, a, score)
        grow_snake(food)
        if sleeps == str('y'):
            sleep(a)
        if hitting_wall() :
            wall += 1
            break
        if hitting_tail() :
            tail += 1
            break
        window.update()
    a = c.create_text(125, 125, text='GAME OVER', fill='white', font=('Helvetica',30))
    b = c.create_text(125, 155, text='Score: '+ str(score), fill='white')
    for i in range(len(snake_parts)):
        c.delete(snake_parts[i])
    del s_dir
    window.update()
    if sleeps == str('y'):
        sleep(1)
    c.delete(apple)
    c.delete(a)
    c.delete(b)
    scores.append(score)
    a = 0
    r += 1
    for i in range(len(scores)):
        a+= scores[i]
    if d < score:
        d = score
    b = a / len(scores)
    if s_ro == str('y'):
        print(r - 1)
    if s_game == str('y'):
        print(f'''Round > {r-1}
Score > {score}
Average > {b}
Highest > {d}
''')
s_range = list()
for i in range(d):
    s_range.append([i + 1, 0])
for i in range(len(scores)):
    s_range[scores[i]-1][1]+= 1
print(f'''
Deaths by wall > {wall}
Deaths by tail > {tail}
% Deaths by wall > {100/(r-1)*wall}
% Deaths by tail > {100/(r-1)*tail}
Average > {b}
Highest > {d}
''')
m_n = 0
for i in range(len(s_range)):
    print(f'''{s_range[i][0]}, {s_range[i][1]}''')
print('''


''')
for i in range(len(s_range)):
    b = str()
    for a in range(s_range[i][1]):
        b += str('.')
    if i >= 9:
        print(f'{i+1} > {b}')
    else :
        print(f'{i+1}  > {b}')


