from random import randint, choice

op_list = ('+', '-', '*', '/')
op = choice(op_list)
a = randint(0,10)
b = randint(0,10)
error = randint(-2,2)
while True:
    if op == '+':
        print(a + b + error)
    elif op == '-':
        print(a - b + error)
    elif op == '*':
        print(a*b + error)
    elif op == '/':
        print(a / b + error)
    break




#2. Ng dùng trả lời

# unser_anwser = input("(T/F)? ").upper()

# if unser_anwser == "Y":
#     if error == 0:
#         print("Yay")
#     else:
#         print("Nay")
# else:
#     if error == 0:
#         print("Yay")
#     else:
#         print("Nay")