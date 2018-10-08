from graphics import *
a1 = 700
b1 = 400
a = 20
b = 20
ventana = GraphWin('ScreenSaver', a1, b1)
ventana.setBackground('white')
circulo = Circle(Point(a, b), 20)
circulo.setFill('blue')
circulo.draw(ventana)
c = bool(True)
x1 = 40
x2 = 40
while 1 == 1:
    if c == True:
        while x1 <= a1 and x2 < b1:
            time.sleep(0.01)
            circulo.move(3, 1)
            x1 += 3
            x2 += 1
        if x1 > 700:
            x1 = 700
        if x2 > 400:
            x2 = 400
        if x1 < 2 * a:
            x1 = 40
        if x2 < 2 * b:
            x2 = 40
        c = False
        circulo.setFill('yellow')
        ventana.setBackground('blue')

    if c == False:
        while x1 <= a1 and x2 < b1:
            time.sleep(0.01)
            circulo.move(-2, 1)
            x1 += -2
            x2 += 1
        if x1 > 700:
            x1 = 700
        if x2 > 400:
            x2 = 400
        if x1 < 2 * a:
            x1 = 40
        if x2 < 2 * b:
            x2 = 40
        c = True
        circulo.setFill('red')
        ventana.setBackground('black')
    if c == True:
        while x1 > 2*a and x2 <= b1:
            time.sleep(0.009)
            circulo.move(-2, -1)
            x1 += -2
            x2 += -1
        if x1 > 700:
            x1 = 700
        if x2 > 400:
            x2 = 400
        if x1 < 2 * a:
            x1 = 40
        if x2 < 2 * b:
            x2 = 40
        c = False
        circulo.setFill('green')
        ventana.setBackground('brown')
    if c == False:
        while x1 < a1 and x2 > 2*b:
            time.sleep(0.008)
            circulo.move(2, -1.5)
            x1 += 2
            x2 += -1.5
        if x1 > 700:
            x1 = 700
        if x2 > 400:
            x2 = 400
        if x1 < 2 * a:
            x1 = 40
        if x2 < 2 * b:
            x2 = 40
        c = True
        circulo.setFill('purple')
        ventana.setBackground('yellow')