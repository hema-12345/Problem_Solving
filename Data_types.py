#1.swap numbers.
"""
a=3
b=2
a,b=b,a
print(a,b)"""
  #or
""" 
a=2
b=5
temp=a
a=b
b=temp
print(a,b)"""


#2.identify data types
"""
a=int(input())
b=input()
c=float(input())
print(type(a),type(b),type(c))"""


#3.calculater
"""
a=int(input())
b=int(input())
operator=input()
if operator=="+":
    print(f"addition{a+b}")
elif operator=="-":
    print(f"subtraction{a-b}")
elif operator=="*":
    print(f"multiplication{a*b}")
elif operator=="/":
    print(f"division{a/b}")
elif operator=="//":
    print(f"floor division{a//b}")
elif operator=="%":
    print(f"modulus{a%b}")
elif operator=="**":
    print(f"exponential{a**b}")
else:
    print(f"invalid operator")"""

#4.salary hike
"""
salary=float(input())
hike=salary*0.15
new_salary=hike+salary
print(f"old salary {salary}")
print(f"new salary {new_salary}")"""


#5.area and perimeter
'''
pi=3.14
r=int(input())
print("area of a circle :",pi*r*r)
print("perimeter of a circle",2*pi*r)'''


#6.ASCII character
"""
char=input()
print(ord(char))"""

#7.check even or odd
"""
a=int(input())
if a%2==0:
    print(f"{a}even")
else:
    print(f"{a}odd")"""


#8.compund assignment
"""
a=5
a+=2
print(a)
a-=2
print(a)
a*=2
print(a)
a/=2
print(a)
a//=2
print(a)
a%=2
print(a)"""

#9.logical operator
"""
age=int(input())
b=input()
if (age>0 and age<120) and b.strip()!=" ":
    print("valid input values")
else:
    print("invalid")"""

#10.Bitwise shift operator.
"""
n=int(input())
print(n<<1)     #where here the given value will be converted into binary bits and shift operator moves the "1" bit based on the 
print(n<<2)     #shift operator it may be left (<<) or right(>>) by the given number 
print(n>>1)     #eg:0000 0010 binary value of 2 
print(n>>2)     #   0000 0100  (2<<1) 4 is the value for 2 left shift 1 as shown.
"""

#11.Bitwise AND,OR,NOT.
"""
a=12
b=5
print(a&b)
print(a|b)
print(a^b)
print(~a)
print(~b)
"""
#12.Data type conversion.
"""
a=10
print(str(a))
print(float(10.0))
print(bool(1))"""

#13.temperature conversion.
"""
a= int(input("Enter choice (1 or 2): "))

if a== 1:
    celsius = float(input("Enter temperature in Celsius: "))
    fahrenheit = (celsius * 9/5) + 32
    print(f"{celsius}°C = {fahrenheit:.2f}°F")

elif a== 2:
    fahrenheit = float(input("Enter temperature in Fahrenheit: "))
    celsius = (fahrenheit - 32) * 5/9
    print(f"{fahrenheit}°F = {celsius:.2f}°C")

else:
    print("Invalid choice. Please enter 1 or 2.")"""


#14.Quotient and reminder
"""
a=10%3
b=10//3
print("reminder: ",a)
print("quotient: ",b)"""


#15.string operations.
"""
a=input()
print(a.upper())
print(a.lower())
print(len(a))
print("m" in a)"""


#16.sum of digits
"""
a=int(input())
sum=0
while a!=0:
    rem=a%10
    sum+=rem
    a//=10
print(sum)"""
  # (or)
"""
a=int(input())
st=str(a)
sum=0
for digit in st:
    sum+=int(digit)
print(sum)
"""


#17.Identity vs equality
"""
a=[1,2,3,4,5]
b=[1,2,3,4,5]
print(a==b)   #it compares values in the sequence
print(a is b)   #it compares memory locations of the lists."""

#18.convert age in years into months and days
"""
n=int(input())
months=n*12
days=n*365
print("age in months: ",months)
print("age in days: ",days)"""

#19.type guessing
"""
x=10+3.5
y="age :"+str(30)
z=True+False+2
print("x =", x, ", Type of x:", type(x))
print("y =", y, ", Type of y:", type(y))
print("z =", z, ", Type of z:", type(z))"""


#20.Bitwise practice (no bin())
"""
n=int(input())
print(~n)   #first convert n value into binary bits and find the 2's complement it will be equal
print(n<<1)   #negotation value that associated with the memory.
print(n>>2)   #it shifts the binary bit "1" leftside to 1 bit position and n>>2 shifts bit moves to right
              #side 2 bit positions  and prints the binary value."""