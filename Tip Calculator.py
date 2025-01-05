print("Welcome to the tip calculator")
B= float(input("What is your bill amount?"))
T=float(input("What percentage tip are you wishing to pay 12, 15, 20?"))
P= int(input("How many people will split the bill?"))
A= B* T/100
total_tip=B+A
total_pay=total_tip/P
print (f"Each person should pay:{total_pay}")