import turtle
from random import randrange
from time import sleep

turtles = 7
racers = []

class Racer(object):
    def __init__(self, color, pos):
        self.color = color
        self.pos = pos
        self.t = turtle.Turtle()
        self.t.pensize(2)
        self.t.turtlesize(1.5)
        self.t.shape('turtle')

        self.t.color(color)
        self.t.penup()
        self.t.setpos(pos)
        self._length = 0

    def move(self):
        random = randrange(5, 40)
        self.pos = (self.pos[0], self.pos[1] + random)
        self.t.pendown()
        self.t.forward(random)
        self._length += abs(random)

    def win(self):
        if self._length > 790:
            print('Ladies & Gentleman', self.color, 'is a winner!')
            sleep(1)
            return True

    def __del__(self):
        pass


def meta_gen():
    meta = turtle.Turtle()
    meta.ht()
    meta.penup()
    meta.goto(350, 360)
    meta.write('Finish Line', font=('Ariel', 15, 'normal'))

    meta.goto(390, 350)
    meta.pendown()
    meta.goto(390, -350)


def countdown():
    n = 3
    count = turtle.Turtle()
    count.ht()
    for i in range(3):
        count.write(n - i, font=('Ariel', 30, 'normal'))
        sleep(1)
        count.clear()
    count.write('Start!', font=('Ariel', 30, 'normal'))
    sleep(1)
    count.clear()


def position_gen():
    a = -300
    for i in range(turtles):
        yield a
        a += 100


def color_gen():
    color = ("red", "green", "blue", 'yellow', 'pink', 'orange', 'purple')
    for i in color:
        yield i


def position():
    color = color_gen()
    pos = position_gen()
    for i in range(turtles):
        racers.append(Racer(next(color), (-400, next(pos))))


def move():
    while True:
        for i in racers:
            Racer.move(i)
            while Racer.win(i):
                return True


def reset():
    print('Do you wanna rematch? - yes/no')
    user_input = input()
    if user_input == 'yes':
        racers.clear()
        turtle.clearscreen()
        main_loop()

    elif user_input == 'no':
        print('See you next time!')
        quit()

    else:
        print('Input correct value')
        reset()


def main_loop():
    meta_gen()
    position()
    countdown()
    if move():
        reset()


main_loop()
