print("WELCOME TO THE TIP CALCULATOR!!!")
total_bill = float(input("What was the total bill?:$ "))
tip = float(input("What was the tip percentage?:"))
total = total_bill+((tip/100)*total_bill)
split = int(input("How many people are splitting the bill?:"))
contribution = total/split
print(f"The amount each member has to pay is ${round(contribution,2)}")

#process of pulling out a charcater from a string is called subscripting
#print("Hello"[2])

'''len("Antony")

print(type("maang"))
print(type(123))
print(type(True))
print(type(31.94))'''

'''print("No of letters in your name :" + str(len(input("What is your name?:"))))'''

'''bmi = 84/1.65**2
print(bmi)
print(int(bmi)) #removes decimal places
print(round(bmi,2)) #rounds of according to value of decimal'''

#input function always takes string as default input


