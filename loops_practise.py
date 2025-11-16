#  1. Write a program using a for loop to print all numbers divisible by 7 between 1 and 200
# num=[i for i in range(1,201) if i%7==0]
# print(num)

# 2.Using a while loop, print the sum of digits of a given integer.
# num=int(input())
# sum=0
# while num!=0:
#     sum+=num%10
#     num//=10
# print(sum)
    
#3. Write a for loop program to count how many vowels are present in a given string
# str1=input()
# total=0
# for i in str1:
#     if i.lower() in "aeiou":
#         total+=1
# print(total)


#4.Using a while loop, reverse a given number without converting it into a string.
# num=int(input())
# rev=0
# while num!=0:
#     rem=num%10
#     rev=rev*10+rem
#     num//=10
# print(rev)

#5.Write a program using a for loop to generate the following pattern:
# *
# **
# ***
# # ****
# n=4
# for i in range(n):
#     for j in range(i+1):
#         print("*",end=" ")
#     print()

# 6. Using a while loop, print the Fibonacci series up to N terms.
# n=int(input())
# a,b=0,1
# for i in range(n): it is for for loop
# while n!=0:
#     print(a,end=" ")
#     a,b=b,a+b
#     n-=1


# def gcd(a,b):
#     if b==0:
#         return a
#     else:
#         return gcd(b,a%b)
# g=gcd(6,15)
# print(g)

# 7. Write a for loop to check if a number is prime or not.
# num=int(input())
# for i in range(2,num):
#     if num%i==0:
#         print("not prime")
#         break
# else:
#     print("prime")


#8.Using a while loop, keep asking the user for a number until they enter a negative number.
# Finally print the total count of positive numbers entered.
# count=0
# while True:
#     num=int(input("enter a number:"))
#     if num<0:
#         break
#     else:
#         count+=1
# print(count)

# 9. Write a for loop program to find the largest element in a list without using built-in max()
# list1=[2,56,34,89,3,2,1,5,100]
# max=list1[0]
# for num in list1:
#     if num>max:
#         max=num
# print(max)

# 10. Using a while loop, print the multiplication table of a number entered by the user (1 to 10).
# num=int(input())
# i=1
# while i<=10:
#     print(f"{num}X{i}={num*i}")
#     i+=1


#11.Write a program using nested for loops to print a 5×5 square of numbers from 1 to 5.
# i=1
# while i<=5:
#     j=1
#     p=1
#     while j<=5:
#         print(p,end=" ")
#         p+=1
#         j+=1
#     print()
#     i+=1
# 12. Using a while loop, calculate the factorial of a number.
# num=int(input())
# fact=1
# while num!=0:
#     fact*=num
#     num-=1
# print(fact)
# 13. Write a for loop to print all even-indexed characters of a string.
# str1=input()
# for i in range(0,len(str1),2):
#     print(str1[i],end="")
    
# 14Using a while loop, keep taking input of numbers and print the running total until the total exceeds
# 100
# sum=0
# while True:
#     num=int(input("enter a number"))
#     sum+=num
#     print(sum)
#     if sum>=100:
#         break

# 15.Write a for loop to count how many elements in a list are greater than the average of the list (do not
# use sum() or len())
# list1=[2,4,56,7,8,4,5,12,45,34,45]
# count=0
# total=0
# for num in list1:
#     total+=num
#     count+=1
# avg=total/count
# t1=0
# for num in list1:
#     if num>avg:
#         t1+=1
# print(t1)

# 16. Using a while loop, find the smallest digit in a number.
# num=int(input())

# while num>0:
#     min_val=9
#     digit=num%10
#     if digit<min_val:
#         min_val=digit
#     num//=10
# print(min_val)

#17.Write a for loop program to print this pattern:
# 1
# 1 2
# 1 2 3
# 1 2 3 4
# for i in range(4):
#     p=1
#     for j in range(i+1):
#         print(p,end=" ")
#         p+=1
#     print()

#18. Using a while loop, print numbers from 1 to 100 but skip multiples of 5.
# i=1
# while i<=100:
#     if i%5!=0:
#         print(i,end=" ")
#     i+=1

#19.Write a for loop to print the ASCII value of each character in a string.
# str1=input()
# for char in str1:
#     print(ord(char),end=" ")
    
#20.Using a while loop, print the sum of the series: 1 + 2 + 3 + ... + n.
# num=int(input())
# sum=0
# while num>=1:
#     sum+=num
#     num-=1
# print(sum)
    