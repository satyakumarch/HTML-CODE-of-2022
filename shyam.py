from turtle import *
import colorsys
bgcolor('gray')
speed(0)
h1 = 0.6
for i in range(300):
    c = colorsys.hsv_to_rgb(h1,1,1)
    color(c)
    h1+=0.005
    for j in range(3):
        circle(i)
        rt(36)
done()