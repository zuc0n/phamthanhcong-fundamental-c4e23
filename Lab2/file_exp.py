content = 'Toi yeu em nhieu lam'

with open("content.txt", "r") as f:
    c = f.read()
    print(c)



# #1. Open File
# f = open("content.txt","w") #open file and set mode in writs
# #2. Write File
# f.write(content)
# #3. Close File
# f.close()