# def fact(n):
#     if n==0 or n==1:
#         return 1
#     else:
#         return n*fact(n-1)
# s=fact(5)
# print(s)



# def sumOfNum(n):
#     if n==1:
#         return 1
#     return n+sumOfNum(n-1)
# print(sumOfNum(5))


# def rev_str(str1):
#     if len(str1)==0:
#         return " "
#     return rev_str(str1[1:-1])+str1[0]
# print(rev_str("hemalakshmi"))




# def fibonacci(n):
#     if n==0:
#         return 0
#     elif n==1:
#         return 1
#     else:
#         return fibonacci(n-1)+fibonacci(n-2)
# for i in range(11):
#     print(fibonacci(i),end=" ")"


# def sum_of_digit(num):
#     if num<=0:
#         return 0
#     return (num%10)+sum_of_digit(num//10)
# print(sum_of_digit(567))


# def palindrome(val):
#     if len(val)<=0:
#         return True
#     elif val[0]!=val[-1]:
#         return False
#     return palindrome(val[1:-1])
# print(palindrome("madam"))
# print(palindrome("frnds"))

#Exponents
# def exp(base,power):
#     if power==0:
#         return 1
#     return base*exp(base,power-1)
# print(exp(2,4))


#gcd
# def gcd(a,b):
#     if b==0:
#         return a
#     else:
#         return gcd(b,a%b)
# a=int(input())
# b=int(input())
# print(gcd(a,b))