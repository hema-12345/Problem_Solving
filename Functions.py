#1.cube number
"""
def cube(n):
    return n**3
num=cube(3)
print(num)"""

#2.Average
'''
def avg(n1,n2):
    return (n1+n2)/2
a=avg(5,5)
print(a)'''


#3.square and square root
''' 
def square(n):
    sq=n**2
    sqr=n**0.5
    return sq,sqr
s=square(5)
print(s)'''


#4.odd
'''
def is_odd(n):
    if n%2!=0:
        return True
    else:
        False
print(is_odd(4))'''


#5.sum of digits
'''
def digit_sum(n):
    sum=0
    while n!=0:
        rem=n%10
        sum+=rem
        n//=10
    return sum
s=digit_sum(12345678)
print(s)'''



#6.default parameter
'''
def greet(name="hema"):
    return "hello,!"
print(greet())'''


#7.power
'''
def power(base,exponent=2):
    return base**exponent
print(power(4))'''

#8.bill
'''
def total(item="sandwich",quantity=1,price=50):
    return quantity*price
print(total('burger',4,100))'''

#9.employee-information
'''
def emp_info(name="raju",age=22,department="ceo"):
    print(f"welcome {name} at age of {age} u become {department}")
emp_info("hema",21,"HR")'''

#10.circle area
'''
def area_circle(radius=1):
    area=3.14*radius**2
    return area
val=area_circle(5)
print(val)'''


#11.loop and return
'''
def even(n):
    sum=0
    for i in range(n+1):
        if i%2==0:
            sum+=i
    return sum
print(even(8))'''


#12.max
'''
def max_value(l):
    return max(l)
a=([9,56,78,45,34])
print(max_value(a))'''

#13.min_max
"""
def min_max(num):
    m=max(num)
    n=min(num)
    return m,n
a=[23,34,12,35,56,45,59]
print(min_max(a))"""

#14.student summary
"""
def student_summary(name="ganesh",marks=[23,45,78,67]):
    total=0
    for i in marks:
        total+=i

    avg=total/len(marks)
    return name,total,avg
print(student_summary())"""

#15.calculator
'''
def calculator(op1,op2,operator="+"):
    if operator=='+':
        sum=op1+op2
        return sum
    elif operator=='-':
        sub=op1-op2
        return sub
    elif operator=='*':
        mul=op1*op2
        return mul
    elif operator=='/':
        div=op1/op2
        return div
    else:
        return None
print(calculator(20,80,'*'))'''

