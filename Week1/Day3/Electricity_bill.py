units = int(input("Enter Units: "))

if units <=100:
   bill = units*1.50
elif units <=200:
   bill = units*2.50

else:
   bill = (100*1.50)+(100*2.50)+((units-200*4)*4.00)

print("Electricity Bill = ₹{:.2f}".format(bill))

