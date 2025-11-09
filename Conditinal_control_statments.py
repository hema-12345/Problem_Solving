#1.Divisibility of 3 and 5
"""
a=int(input())
if a%3==0 and a%5==0:
    print(f"{a} is divisible by 3 and 5")
else:
    print("try with another number")"""


#2.compare 2 numbers.
"""
a=int(input())
b=int(input())
if a>b:
    print(f"{a}  is greater")
else:
    print(f"{b} is greater")"""

#3.grade
"""
a=int(input())
if a>=85:
    print(f"u got A grade")
elif a>=65:
    print("u got B grade")
elif a>=35:
    print("u got C grade ")
else:
    print("failed bro")"""

#4.check positive and even
"""
a=int(input())
if a>0 and a%2==0:
    print(f"{a} is positive and also even number")
else:
    print(" it is not")"""

#5.check age
"""
a=int(input())
if a>0 and a<13:
    print("you are a child")
elif a>=13 and a<=19:
    print("you are a teenage")
elif a>=20 and a<=120:
    print("you are a adult")
else:
    print("entered a invalid input value")"""
   


   
#control statements
 
#1.break
"""
a=[1,23,45,22,45,46]
for i in a:
    if i%2==0:
        print(i)
        break"""


#2.password 
"""
n=3
actual_password="Hema@123"
for i in range(3):
    password=input("enter password")
    if password==actual_password:
        print("Access granted")
        break
    else:
        print("Entered incorrect password")
else:
    print("locked out") """

#3.infinite loop
"""
while True:
    a=input()
    if a=="exit":
        print("loop exited")
        break"""

#4.continue
"""
a=[1,-2,3,4,-4,-5,-6,-7,-9]
for digit in a:
    if digit<0:
        continue
    else:
        print(digit,end=" ")"""

#5.skip vowels
'''
string=input()
vowels=['A','E','I','O','U','a','e','i','o','u']
for char in string:
    if char in vowels:
        continue
    else:
        print(char,end=" ")'''

#6.divisibility
"""
for i in range(1,51):
    if i%3==0 and i%5!=0:
        continue
    else:
        print(i,end=" ")"""

#7.function
"""
def process_data():
    pass

process_data()

#8.class
class User():
    pass

#9.for loop
for i in range(1,6):
    pass
"""

#10.mixed challenge
"""
a=[1,23,56,67,34,56,78,32,98,23,45]
for digit in a:
    if digit%2!=0:
        continue
    elif digit<=50:
        break
    elif digit==0:
        pass
    else:
        print(digit)
else:
    print("No condition  matches")"""

#11.word match
a=['hi', 'cat', 'wait', 'dog', 'end', 'zebra'] 
for i in a:
    if len(i)<3:
        continue
    elif i=="end":
        break
    elif i=="wait":
        pass
    else:
        print(i)
