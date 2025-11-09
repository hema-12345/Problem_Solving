# # 1.neon number
# num=int(input())
# sqr=num**2
# sum=0
# while sqr!=0:
#     rem=sqr%10
#     sum+=rem
#     sqr//=10
# if sum==num:
#     print("its %d a neon number" %(num))
#     #print("its {} a neon number".format(num))
# else:
#     print("not a neon number")


# # 2.sunny number
# number=int(input())
# sqr_root=int((number+1)**0.5)
# if sqr_root**2==(number+1):
#     print(f"{number} is a sunny number ")
# else:
#     print("{} is not a sunny number".format(number))



# # 3.harshad(niven) number
# number=int(input())
# sum=0
# temp=number
# while temp!=0:
#     rem=temp%10
#     sum+=rem
#     temp//=10
# if number%sum==0:
#     print("%d is a harshad number"%(number))
# else:
#     print("{} is not a niven number".format(number))



# # 4.Armstrong number
# for num in range(lower_limit,upper_limit+1):
#     copy_num=num
#     total=0


#     while copy_num!=0:
#         digit=copy_num%10
#         total+=(digit**3)
#         copy_num//=10

#     if num==total:
#         print(num)



# # 5.Automorphic number
# num=int(input())
# def auto_morphic(num):
#     sqr_root=num**2
#     while num>0:
#         if (num%10)!=(sqr_root%10):
#             return False
#         num//=10
#         sqr_root//=10
#     return True
# n=int(input())
# if auto_morphic(n):
#     print("automorphic")
# else:
#     print("not")

        

# 6.perfect number
# num=int(input())
# sum=0
# temp_num=num
# for i in range(1,temp_num):
#     if temp_num%i==0:
#         sum+=i
#     print(sum)
# if num==sum:
#     print("perfect number")
# else:
#     print("not")


# 7.strong number
# num=int(input())
# temp=num
# sum=0
# while temp!=0:
#     fact=1
#     dig=temp%10
#     for i in range(1,dig+1):
#         fact*=i
#     sum+=fact
#     temp//=10
# if num==sum:
#     print("strong")
# else:
#     print("not")




# 8.spy number
# num=int(input())
# sum=0
# mul=1
# temp=num
# while num!=0:
#     rem=num%10
#     sum+=rem
#     mul*=rem
#     num//=10
# if sum==mul:
#     print(f"{temp} is a spy number")
# else:
#     print(f"{temp} is not spy number")




# # 9.BUZZ number
# num=int(input())
# if num%7==0 or num%10==7:
#     print("it is a buzz number ")
# else:
#     print("not")


