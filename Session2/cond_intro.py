yob = int(input("Your year of birth?"))
age = 2018 - yob
print(age)
if age <= 10:
    print("Kinder")
elif age <= 20:
    print("Junger")
else:
    print("Erwachsen")
