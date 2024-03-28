import random
import math

earth = makeWorld()
tur = makeTurtle(earth)

def square():
  global tur
  for i in range(4):
    tur.forward(100)
    tur.turnLeft()

def rectangle():
  for i in range(2):
    tur.forward(100)
    tur.turnLeft()
    tur.forward(50)
    tur.turnLeft()

def triangle(): #This function actually works for any number of sides
  sides = 3
  compAngle = 360
  for i in range (sides):
    tur.forward(100)
    tur.turn(compAngle/sides)

#def rightTriangle():
  #SOH CAH TOA
#  a = 100
#  b = 90
#  c = sqrt((a^2)*(b)^2)
#  B = math.degrees(math.acos(a/c))
#  A = math.degrees(math.asin(a/c))
#  tur.forward(a)
#  tur.turn(int(B))
#  tur.forward(int(c))
#  tur.turn(int(A))
#  tur.forward(b)
#The error value is: math domain error, I don't understand.

def rightTriangle():
  a = 100
  b = 95
  c = 138
  tur.turn(180)
  tur.forward(100)
  tur.turn(90)
  tur.forward(95)
  tur.turn(180-46)
  tur.forward(138)


def pentagon():
  sides = 5
  compAngle = 360
  for i in range (sides):
    tur.forward(100)
    tur.turn(compAngle/sides)

def hexagon():
  sides = 6
  compAngle = 360
  for i in range (sides):
    tur.forward(100)
    tur.turn(compAngle/sides)

def octagon():
  sides = 8
  compAngle = 360
  for i in range (sides):
    tur.forward(100)
    tur.turn(compAngle/sides)

def myriagon():
  sides = 360
  compAngle = 360
  for i in range (sides):
    tur.forward(3)
    tur.turn(compAngle/sides)