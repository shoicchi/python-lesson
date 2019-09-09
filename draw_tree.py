#!/user/bin/env python
# _*_ coding: utf-8 _*_

from turtle import*
def tree(length):
    if length > 5:
        forward(length)
        right(20)
        tree(length-15)
        left(40)
        tree(length-15)
        right(20)
        backword(length)

color("green")
left(90)
backword(150)
tree(120)

input('type to exit')
