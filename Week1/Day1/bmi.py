weight = float(input("Enter weight (kg): "))
height = float(input("Enter height (m): "))

bmi = weight/(height*height)

print("BMI =",round(bmi, 2))