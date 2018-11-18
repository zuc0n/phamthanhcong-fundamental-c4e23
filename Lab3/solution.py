#1. tạo 1 câu đố cho người dùng
from random import randint, choice
from function_intro import eval

def generate_quiz():
    x = randint(0,10)
    y = randint(0,10)
    error = randint(-2,2)
    o = choice(['+', '-', '*', '/'])
    r =  eval(x, y, o) + error
   

    return x, y, r, o

a, b, op, r = generate_quiz()
print(a, op, b, "=", r)
#2. Ng dùng trả lời

unser_anwser = input("(T/F)? ").upper()

if unser_anwser == "Y":
    if error == 0:
        print("Yay")
    else:
        print("Nay")
else:
    if error == 0:
        print("Yay")
    else:
        print("Nay")