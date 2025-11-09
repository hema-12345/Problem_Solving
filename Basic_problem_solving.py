# #1.
# n=int(input())
# fact=1
# for i in range(1,n+1):
#     fact*=1
# print(fact)

# # #2.sum n numbers
# n=int(input())
# sum=0
# for i in range(1,n+1):
#     sum+=i
# print(sum)

# #3.
# num=int(input())
# rev=0
# while num>0:
#     dig=num%10
#     rev=rev*10+dig
#     num//=10
# print(rev)

# #4.
# num=int(input())
# temp=num
# rev=0
# while num>0:
#     dig=num%10
#     rev=rev*10+dig
#     num//=10
# if temp==rev:
#     print(f"{rev} is a palindrome")
# else:
#     print(f"not a palindrome")


# #5.
# n=int(input())
# a=0
# b=1
# for i in range(n):
#     print(a,end=" ")
#     a,b=b,b+a

# #6.
# user_name="Hema0505"
# pass_word="123456"
# usn=input()
# pwd=input()
# if user_name==usn and pass_word==pwd:
#     print("login successful")
# else:
#     print("invalid credentials")


# #7.
# a=[1,3,5,2,6,7,34,23]
# sum=0
# for char in a:
#     sum+=char
# print(sum)



# #8.
# a=[12,34,3,234,345,567,321,543]
# b=[]

# for char in a:
#     rev=0
#     temp=char
#     while temp>0:
#         dig=temp%10
#         rev=rev*10+dig
#         temp//=10
#     b.append(rev)
# print(b)


# #9.
# n=int(input())
# sqr=n**2
# sum=0
# while sqr>0:
#     dig=sqr%10
#     sum+=dig
#     sqr//=10
# if sum==n:
#     print("neon number ")
# else:
#     print("not a neon number")


# #10.
# n=int(input())
# per_sq=(n+1)**0.5
# if (per_sq**2)==(n+1):
#     print(n,"it is a sunny number")
# else:
#     print("not a sunny number")


# words={1:"this",2:"is",3:"a",4:"python",5:"class"}
# for index,(key,value )in enumerate(words.items()):
#     print(f"{index},{value}")


# words=(1,"this","is","python")
# for val,item in enumerate(words):
#     print(f"{val}--->{item}")