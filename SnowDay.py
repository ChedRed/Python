from turtle import *
from random import *
def makeSnowflakeRNG(X):
    t = Turtle()
    t.speed(100)
    t.pensize(2)
    t.pencolor("Firebrick")
    def snowflakeHand(C):
        t.right(25)
        t.forward(C)
        t.backward(C)
        t.left(50)
        t.forward(C)
        t.backward(C)
        t.right(25)
    def snowflakeArmRNG():
        import random
        for E in range(X):
            for I in range(4):
                t.forward(20)
                a = random.randint(-200,200)
                snowflakeHand(a)
            t.backward(80)
            t.right(360 / X)
    snowflakeArmRNG()
def makeSnowflake(X):
    t = Turtle()
    t.speed(100)
    t.pensize(2)
    t.pencolor("Firebrick")
    def snowflakeHand(C):
        t.right(25)
        t.forward(C)
        t.backward(C)
        t.left(50)
        t.forward(C)
        t.backward(C)
        t.right(25)
    def snowflakeArm():
        for E in range(X):
            for I in range(4):
                t.forward(20)
                snowflakeHand((I + 1) * 20)
            t.backward(80)
            t.right(360 / X)
    snowflakeArm()
makeSnowflake()
input("Waitiing for enter key...")