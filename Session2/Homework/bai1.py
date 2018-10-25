height = int(input("height ="))
weight = int(input("weight ="))
chieucao = height / 100
bmi = weight / (chieucao * 2)
if bmi < 16:
    print("Severly underweight")
elif bmi < 18.5:
    print("Underweight")
elif bmi < 25:
    print("Normal")
elif bmi < 30:
    print("Overweight")
else:
    print("Obese")