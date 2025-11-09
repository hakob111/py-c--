from graph import *



penColor('red')
brushColor('green')
circle(200, 150, 50)


print("enter the rectagle coedinats ")
x = int(input("x = "))
y = int(input("y = "))
a = 20
rectangle(x, y, x+a, y+a)
run()

""" tasks & exercises """

""" task 1  Determine the coordinates of the pixels that make up the segments:
    a) (10, 20) -- (10, 15)  b) (10, 20) -- (15, 21)
    c) (10, 20) -- (5, 15)   d) (10, 20) -- (15, 22) 
    that is, Bresenham's algorithm
    P_0 = 2Delta y - Delta x
"""

x1, y1, x2, y2 = 10, 20, 10, 15

difx = x2 - x1
dify = y2 - y1

x, y = x1, y1
pixels = [(x, y)]
P = 2 * dify-difx

P_inc_y = 2 * (dify - difx)
p_inc_x = 2 * dify

for i in range(abs(difx + dify)):
    x += 1
    if P < 0:
        P += p_inc_x
    else:
        y += 1
        p += P_inc_y
    pixels.append((x, y))

print(pixels)


"""Draw a house """
x = 25
y = 65
penColor('black')
brushColor('blue')
polygon( [(x-10,y), (x+50,y-50), (x+110,y), (x-10,y)] )
brushColor("green")
rectangle(x, y, x+100, y+100 )
penSize(3)
brushColor('black')
penColor('white')
rectangle(x+10, y+10, x+50, y+50)
line(x+10, y+25, x+50, y+25)
line(x+30, y+25, x+30, y+50)
run()


"""Run it to see what it draws. """

x = 40
y = 60
radius = 15
penColor("black")
brushColor("red")

circle(x, y, radius)
brushColor("purple")
polygon([(x+radius, y), (x+radius+50, y-30), (x+radius+100, y), (x+radius, y)])
brushColor("green")
polygon([(x+radius, y), (x+radius+50, y+30), (x+radius+100, y), (x+radius, y)])
brushColor("yellow")
circle(x+radius+100+radius, y, radius)
run()


"""Draw a house with functions """
def frame(x, y):
    penColor('black')
    brushColor("gray")
    rectangle(x, y, x+100, y+100)
    

def roof(x, y):
    penColor('black')
    brushColor('pink')
    polygon([(x-20, y), (x+55, y-50), (x+120, y, x-10, y)])

def house_window(x, y):
    penColor('white')
    brushColor('black')
    penSize(3)
    rectangle(x+10, y+10, x+50, y+50)
    line(x+10, y+20, x+50, y+20)
    line(x+30, y+20, x+30, y+50)
    penSize(1)


def house(x, y):
    frame(x, y)
    roof(x, y)
    house_window(x, y)
canvasSize(800, 800)
house(40, 50)
house(200, 50)
house(360, 50)
house(520, 50)
run()

penColor("black")
brushColor('green')
polygon([(100, 50), (180, 50), (100, 100), (100, 50)])
brushColor("red")
polygon([(100, 50), (180, 10), (100, 10), (100, 50)])
brushColor("blue")
polygon([(100, 50), (20, 100), (20, 50), (100, 50)])
run ()


penColor("black")
brushColor('green')
polygon([(100, 50), (180, 50), (140, 90), (100, 50)])
brushColor("red")
polygon([(180, 50), (260, 50), (220, 90), (180, 50)])
brushColor("blue")
polygon([(140, 90), (220, 90), (180, 130), (140, 90)])
run ()