#1.Juice shop Discount
"""
a=int(input())
total=float(input())
b=input()
if a>2:
    if b=="regular":
        discount=total*0.15
        total=total-discount
        print(total)
    else:
        discount=total*0.5
        total=total-discount
        print(total*0.5)
else:
    print("sorry no discount")"""

#2.Fuel check
"""
fuel=int(input("enter fuel level "))
if fuel<25:
    vehicle=input("vehicle type ")
    if vehicle=="car":
        print("refuel soon at a petrol station")
    elif vehicle=="bike":
        print("refuel at nearest pump")
    else:
        print("vehicle not found")
else:
    print("fuel is not below 25%") """

#3.schlorship eligibilty
"""
grade=int(input("enter your grade"))
if grade>85:
    income=int(input("enter your income "))
    if income>300000:
        print("eligible for full scholarship")
    elif income>300000 and income<600000:
        print("eligible for half schlorship")
    else:
        print("no scholarship")
else:
    print("you got below 85 can't proceed for scholarship")"""

#4.shopping cart offer
"""
total_cart=float(input("enter cart value "))
if total_cart>1000:
    payment_method=input("enter cash or upi ")
    if payment_method=="cash":
        offer=total_cart*0.1
        print(f" you got {offer} rupees")
    elif payment_method=="upi":
        offer=total_cart*1.5
        print(f" you got {offer} rupees")
    else:
        print("check with payment method.")
else:
    print(f" Add items worth of {1000-total_cart} to get offers")
"""

#5.restaurant entry check
"""
age=int(input())
if age>=18:
    vaccinated_status=input("enter yes or no")
    if vaccinated_status=="yes":
        print("Dine In")
    else:
        print("Take Away")
else:
    print("you must be at atleast")"""

#6.sports tournments
"""
age=int(input())
if age>14 and age<18:
    height=int(input("enter height in centimeters"))
    if height==160:
        print("eligible")
    else:
        print("you are too short")
else:
    print("age out of range")"""
              #OR
"""
age=int(input())
if 14< age <18:
    height=int(input("enter height in centimeters"))
    if height==160:
        print("eligible")
    else:
        print("you are too short")
else:
    print("age out of range")"""


#TERNARY OPERATOR

#1.TRAFFIC LIGHT
"""
Color=input("enter color")
print("Go" if Color=="green" else "stop")"""

#2.movie ticket
'''
age=int(input())
print("adult ticket" if age>=18 else "child ticket")

'''

#3.discount offer
"""
amount=int(input())
print("you get a free gift" if amount>=500 else "no gift")
"""

#4.delivry fee
"""
location=input("enter the location local or non local")
print("Rs.20 delivery fee" if location=="local" else "Rs.50 delivery fee")
"""

#5.fever check
"""
temperature=float(input("enter body temperature "))
print("High Fever" if temperature>=100 else "Normal")"""

#6.time based greeting.
"""
time=int(input("enter hour in 24-hour format"))
print("good morning" if time<12 else "good afternoon" if 12 <time< 17 else "good evening")"""


#7.bonus challenge
"""
units=int(input())
if units<100:
    print("free")
elif 100<units<300:
    usage=input("resident or commercial")
    if usage=="resident":
        print("Rs.5 per unit")
    else:
        print("Rs.8 per unit")
else:
    print("Rs.10 per unit flat")"""