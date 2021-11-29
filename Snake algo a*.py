from tkinter import *
from random import randint
from time import sleep
from math import dist
window=Tk()
window.title('Snake')
c=Canvas(window, width=255, height=255, bg='black')
c.pack()
scores=list()
r = 1
d = 0
wall = 0
tail = 0
def c_scan(x1, y1, x2, y2, scaned, walls, squares, s_scaned):
    if [x1, y1] not in scaned and [x1, y1] not in walls and x1>=0 and y1>=0 and x1<len(squares) and y1<len(squares[1]):
        if [x1, y1] in s_scaned:
            if squares[x1][y1][1]>squares[x2][y2][1]+(5):
                squares[x1][y1][1]=squares[x2][y2][1]+(5)
        else:
            squares[x1][y1][1]=squares[x2][y2][1]+(5)
            s_scaned.append([x1, y1])
    return scaned, s_scaned
def scan(block, scaned, walls, squares, s_scaned):
    scaned, s_scaned=c_scan(block[0]+1, block[1], block[0], block[1], scaned, walls, squares, s_scaned)
    scaned, s_scaned=c_scan(block[0]-1, block[1], block[0], block[1], scaned, walls, squares, s_scaned)
    scaned, s_scaned=c_scan(block[0], block[1]+1, block[0], block[1], scaned, walls, squares, s_scaned)
    scaned, s_scaned=c_scan(block[0], block[1]-1, block[0], block[1], scaned, walls, squares, s_scaned)
    return scaned, s_scaned, squares
def choose(s_scaned, squares, scaned, end):
    a=list()
    current_low=squares[s_scaned[0][0]][s_scaned[0][1]][1]+squares[s_scaned[0][0]][s_scaned[0][1]][2]
    for i in range(len(s_scaned)):
        c_check=squares[s_scaned[i][0]][s_scaned[i][1]][1]+squares[s_scaned[i][0]][s_scaned[i][1]][2]
        if c_check<current_low:
            current_low=c_check
            a=[s_scaned[i]]
        elif c_check==current_low:
            a.append(s_scaned[i])
    d=list()
    c_low=squares[a[0][0]][a[0][1]][2]
    for i in range(len(a)):
        c_check=squares[a[i][0]][a[i][1]][2]
        if c_check<c_low:
            c_low=c_check
            d=[a[i]]
        elif c_check==c_low:
            d.append(a[i])
    b=randint(0, len(d)-1)
    s_scaned.remove(d[b])
    scaned.append(d[b])
    if d[b]==end:
        return True, s_scaned, squares, scaned
    return False , s_scaned, squares, scaned
def path2(x1, y1, x2, y2, scaned, squares):
    if [x1, y1] in scaned and squares[x1][y1][1]<squares[x2][y2][1]:
        return True, [x1, y1]
    else:
        return False, 0
def path1(block, scaned, squares, path):
    a=[False, False, False, False]
    b=[0, 0, 0, 0]
    sm=list()
    a[0], b[0]=path2(block[0]+1, block[1], block[0], block[1], scaned, squares)
    a[1], b[1]=path2(block[0]-1, block[1], block[0], block[1], scaned, squares)
    a[2], b[2]=path2(block[0], block[1]+1, block[0], block[1], scaned, squares)
    a[3], b[3]=path2(block[0], block[1]-1, block[0], block[1], scaned, squares)
    for i in range(4):
        if a[i]:
            sm.append(b[i])
    a=randint(0, len(sm)-1)
    path.append(sm[a])
    return path
def test_walls(start, walls):
    a=[0, 0, 0, 0]
    a[1]=tester([start[0]+1, start[1]], walls, 2)
    a[3]=tester([start[0]-1, start[1]], walls, 4)
    a[2]=tester([start[0], start[1]+1], walls, 3)
    a[0]=tester([start[0], start[1]-1], walls, 1)
    a.sort(key= lambda x: x[1])
    for i in reversed(a):
        if i[0] != 0:
            return i[0]
    return 1
def test_wall(block, walls, val):
    if block in walls:
        return 0
    else:
        return val
def test_temp_wall(block, walls):
    a=0
    a+=test_wall([block[0]+1, block[1]], walls, 1)
    a+=test_wall([block[0]-1, block[1]], walls, 1)
    a+=test_wall([block[0], block[1]+1], walls, 1)
    a+=test_wall([block[0], block[1]-1], walls, 1)
    return a
def tester(block, walls, val):
    a=test_wall(block, walls, val)
    if a!=0:
        b=test_temp_wall(block, walls)
        return [a, b]
    else:
        return [0, 0]
s_game = input('Show averages > ')
s_ro = input('Show rounds > ')
sleeps = input('Sleep > ')
s_a=input('Show Algo > ')
for i in range(int(input('Rounds > '))):
    snake_parts = list()
    sp_1 = c.create_rectangle(115, 115, 125, 125, fill='white')
    snake_parts.append(sp_1)
    s_dir = list()
    s_dir.append(2)
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
        squares=list()
        walls=list()
        for x in range(27):
            x1=(x*10)
            temp=list()
            for y in range(27):
                y1=(y*10)
                temp.append([0, 0, 0])
                if x==0 or x==26 or y==0 or y==26:
                    walls.append([x, y])
            squares.append(temp)
        x, y=get_coords(apple[0])
        end=[int(x//10), int(y//10)]
        x, y=get_coords(snake_parts[0])
        start=[int(x//10), int(y//10)]
        for x in range(len(squares)):
            for y in range(len(squares[0])):
                squares[x][y][2]=dist([x*10, y*10], [end[0]*10, end[1]*10])
        scaned=[start]
        s_scaned=list()
        for i in snake_parts[1:]:
            x,y=get_coords(i)
            walls.append([int(x//10), int(y//10)])
        answer=True
        while True:
            scaned, s_scaned, squares=scan(scaned[-1], scaned, walls, squares, s_scaned)
            if len(s_scaned)==0:
                answer = False
                break
            a, s_scaned, squares, scaned=choose(s_scaned, squares, scaned, end)
            if a:
                break
        path=[end]
        if answer:
            while True:
                path=path1(path[-1], scaned, squares, path)
                if path[-1]==start:
                    break
        trolor=[]
        if s_a =='y':
            for i in path[1:-2]:
                trolor.append(c.create_rectangle((i[0]*10)-5, (i[1]*10)-5, (i[0]*10)+5, (i[1]*10)+5, fill='grey'))
        x, y=get_coords(snake_parts[0])
        x=int(x//10)
        y=int(y//10)
        if len(path)>1:
            if path[-2][0]>x:
                del s_dir[0]
                s_dir.insert(0, 2)
            elif path[-2][0]<x:
                del s_dir[0]
                s_dir.insert(0, 4)
            elif path[-2][1]>y:
                del s_dir[0]
                s_dir.insert(0, 3)
            elif path[-2][1]<y:
                del s_dir[0]
                s_dir.insert(0, 1)
        else:
            del s_dir[0]
            abcd=test_walls(start, walls)
            s_dir.insert(0, abcd)
        return trolor
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
    food = 0
    a=0.1
    score = 0
    while True:
        food = grow_apple(food)
        fan=turn_snake()
        move_snake()
        food, a, score = eating_apple(food, a, score)
        grow_snake(food)
        if sleeps == str('y'):
            sleep(a)
        window.update()
        for i in fan:
            c.delete(i)
        if hitting_wall() :
            wall += 1
            break
        if hitting_tail() :
            tail += 1
            break
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
