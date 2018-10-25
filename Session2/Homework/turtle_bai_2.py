
from turtle import *
speed(0)
for i in range(3, 7):

    if i%2 == 0:
        color('red')
    else:
        color('blue')
    
    for x in range(i):
        forward(50)
        left(360/i)

mainloop()