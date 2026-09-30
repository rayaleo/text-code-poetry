"""
              *****       *****
           **********   **********
         *****************************
        *******************************
       *********************************
       *********************************
        ***********heartbeat***********
         *****************************
           *************************
             *********************
               *****************
                 *************
                   *********
                     *****
                       *
"""
import turtle
import time


monitor = turtle.Screen()
monitor.bgcolor("black")
monitor.title("heartbeat")
monitor.setworldcoordinates(0, -120, 900, 120)

pulse = turtle.Turtle()
pulse.speed(0)
pulse.color("lime")
pulse.pensize(3)

morning = []
pressure = []
distractions = []
moments = []

beats = 0

def measure_pulse():
    global beats
    beats += 1

    pulse.clear()
    pulse.penup()
    pulse.goto(100, 0)
    pulse.pendown()

    points = [
        (100, 0),
        (120, 0),
        (135, 18),
        (150, -15),
        (170, 75),
        (190, -45),
        (210, 25),
        (230, 0),
        (255, 0)
    ]

    for x, y in points:
        pulse.goto(x, y)
        time.sleep(0.04)

    print("/\\__/\\/\\__")
    time.sleep(0.4)


def notice(moment):
    distractions.append(moment)
    print(moment)
    time.sleep(0.25)
    measure_pulse()


def carry(weight):
    pressure.append(weight)
    print(weight)
    time.sleep(0.25)
    measure_pulse()


def lambast(moment):
    moments.append(moment)
    print(moment)
    time.sleep(0.25)
    measure_pulse()


def recover():
    print("breathing room")
    time.sleep(0.25)

    pulse.color("cyan")
    pulse.clear()
    pulse.penup()
    pulse.goto(100, 0)
    pulse.pendown()

    points = [
        (100, 0),
        (125, 5),
        (150, -3),
        (175, 4),
        (200, 0),
        (230, 0)
    ]

    for x, y in points:
        pulse.goto(x, y)
        time.sleep(0.08)

    print("/\\________")
    time.sleep(0.4)

    pulse.color("lime")


def start_day():
    print("morning")
    time.sleep(0.5)

    notice("alarm")
    carry("tomorrow's deadline")

    print()
    print("finding a pattern...")
    time.sleep(0.5)

    carry("one more thing")
    notice("a presentation due today")

    notice("running late")
    carry("the clock's past 8")

    lambast("an assignment unfinished")
    notice("a song through the headphones")

    lambast("")

    recover()

    print("variation detected")
    time.sleep(0.3)

    measure_pulse()

    print("rhythm restored")
    time.sleep(0.3)

    measure_pulse()

    print("still responding")
    time.sleep(0.5)


start_day()

print()
notice("lunch break")
lambast("card got declined")
print("the day continues...")
time.sleep(0.5)

notice("clock moves past 11")
lambast("time spent at the courts")
lambast("rush to the computer")
lambast("made it by the deadline")

recover()

print()
print("rhythm stable")
time.sleep(0.4)

measure_pulse()

print("nothing is still")
time.sleep(0.4)

measure_pulse()

print("everything is moving")
time.sleep(0.5)

turtle.done()