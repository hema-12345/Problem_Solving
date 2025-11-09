#variables
'''
name="hema lakshmi"
print(f"hello {name} ,Hope u doing great")'''

'''num1=129
num2=4608
print(num1+num2)'''


'''price=450
quantity=3
print(price*quantity)'''


'''age=22
print(f"wait {100-age} years to turn 100")'''


'''a,b=5,6
a,b=b,a
print(a,b)'''



#data types
'''fruits=["apple","grapes","orange"]
print(fruits[1])'''



'''string="my is name is hema ankamreddy."
print(len(string))'''


'''tuple=(1,23,45,67,89)
print(max(tuple))'''

'''
dict={"hema":97,"lakshmi":78,"anjali":45}
print(dict["lakshmi"])'''

'''
str="143"
str2=int(str)*2
print(str2)'''


'''num=int(input())
if num>0:
    print("positive")
else:
    print("negative")'''

'''age=int(input())
if age<=13:
    print("child") 
elif age>13 and age<=19:
    print("teenager")
else:
    print("adult")'''


'''year=int(input())
if year%4==0 or year%400==0 and year%100!=0:
    print(f"{year} is a leap year")
else:
    print("not a leap year")'''


'''marks=int(input())
if marks>=40:
    print("pass")
else:
    print("fail")'''

'''for i in range(1,11):
    if i==5:
        continue
    print(i)'''

'''for i in range(1,20):
    if i==13:
        break
    print(i)'''


'''for i in range(2,11,2):
    print(i)'''


'''for i in range(1,6):
    pass'''

'''while True:
    a=input()
    if a.lower()=="exit":
        break'''

'''for i in range(1,11):
    print(i)'''

'''i=10
while i>0:
    print(i)
    i-=1'''

'''sum=0
for i in range(1,101):
    sum+=i
print(sum)'''


'''list=[12,34,45,56,78]
for ele in list:
    print(ele)'''


'''n=int(input())
for i in range(1,11):
    print(f"{n} x {i}={n*i}")'''


'''def greet(name):
    print(f"hello {name}")
greet('hema')'''


'''def sum(a,b):
    print(a+b)
sum(4,5)'''

'''def evenorodd(num):
    if num%2==0:
        print("even")
    else:
        print("odd")
evenorodd(9)'''

'''def m(l1):
    print(max(l1))
m([1,23,45,67,89])'''

'''def fact(n):
    fact=1
    for i in range(1,n+1):
        fact*=i
    print(fact)
fact(5)'''


# def peak(n):
#     peak=n[0]
#     for i in range(len(n)):
#         if i==len(n)-1:
#             break
#         if i==0:
#             if n[i]<n[i+1]:
#                 peak=n[i+1]
#             else:
#                 peak=n[i]
#         else:
#             if n[i]<n[i+1]:
#                 if n[i+1]>peak:
#                     peak=n[i+1]
#             else:
#                 if n[i]>peak:
#                     peak=n[i]
#     return peak
# p=peak([1,2,34,20,2])
# print(p)

# def freq_str(string):
#     d={}
#     for char in string:
#         if char in d:
#             d[char]+=1
#         else:
#             d[char]=1
#     max_char=None
#     max_val=0
#     for key,value in d.items():
#         if value>max_val:
#             max_val=value
#             max_char=key
#     return max_char,max_val
# print(freq_str("hemalakshmi"))