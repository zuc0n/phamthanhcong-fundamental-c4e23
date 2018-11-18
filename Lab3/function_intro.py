# def add(a, b):
#     r = a + b
   
#     return r

# # call function

# # s = add(9,10)
# # print(s)

def eval(a,b, op):
    if op == '+':
        r = a + b 
    elif op == '-':
        r = a - b 
    elif op == '*':
        r = a*b 
    elif op == '/':
        r = a / b
    else:
        print('Unsupported Operator')
    return r

# s = eval(4,5, '-') 
# print(s)




