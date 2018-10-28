yob_string = input("Year of birth? ")
while not yob_string.isdigit():
    print("Invalid Value")
    yob_string = input("Year of birth? ")
yob = int(yob_string)
age = 2018 - yob

print(age)
