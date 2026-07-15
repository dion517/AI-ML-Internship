english = int(input("Enter English marks: "))
math = int(input("Enter Math marks: "))
science = int(input("Enter Science marks: "))
social = int(input("Enter Social marks: "))
computer = int(input("Enter Computer marks: "))

total = english + math + science + social + computer

average = total / 5

percentage = (total / 500) * 100

print("Total =", total)
print("Average =", average)
print("Percentage =", percentage, "%")