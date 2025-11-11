      #REVERSE A NUMBER
# num=123
# rev=0
# while num!=0:
#     rem=num%10
#     rev=rev*10+rem
#     num//=10
# print(rev)


#SORT HALF INTO ASCENDING AND REMAINING INTO DESCENDING ORDER
# arr=[4,6,2,1,6,9,0,1,34,56,2]
# mid=len(arr)//2
# ans=[]
# first=arr[:mid]
# second=arr[mid:]
# first.sort()
# second.sort()
# ans=first+second[::-1]
# print(ans)


# SECOND LARGEST AND SECOND SMALLEST
# arr=[5,6,3,2,8,1,0]
# arr.sort()
# print(f"second_max={arr[-2]} and second smallest: {arr[1]}")


# REMOVING PARANTHESIS IN A LIST
# str1="a+b-(c*d)+f"
# str2=""
# for char in str1:
#     if char not in ['(',')','()']:
#         str2 += char
# print(str2)


# SORTING STRING
# str1="daskgrf"
# list1=list(str1)
# list1.sort()
# print("".join(list1))


# DISPLAYING ONLY DUPLICATE VALUES
# list1=[2,3,5,6,4,2,4,6,72,1,2,2,2]
# duplicate=[]
# for i in list1:
#     if list1.count(i)>1 and i not in duplicate:
#         duplicate.append(i)
# print(duplicate)



# list1=[2,3,5,6,4,2,4,6,72,1,2,2,2]
# dup=[]
# uni=[]
# for i in list1:
#     if list1.count(i)==1:
#         uni.append(i)
#     elif list1.count(i)>1 and i not in dup:
#         dup.append(i)
# print(dup)
# print(uni)

# FREQUENCY COUNT
# list1=[2,3,5,6,4,2,4,6,72,1,2,2,2]
# dict1={}
# count=1
# for val in list1:
#     if val not in dict1:
#         dict1[val]=count
#     else:
#         dict1[val]=count+1
# print(dict1)

# ONLY RETURNING CHARACTERS
# str1='abc$123def*'
# str2=""
# for num in str1:
#     if 97<=ord(num)<=122:
#         str2+=num
# print(str2)


# list1=[2,3,5,6,4,2,4,6,72,1,2,2,2]
# dict1={}
# count=1
# for val in list1:
#     if val not in dict1:
#         dict1[val]=1
#     else:
#         dict1[val]+=1
# print(dict1)
# print(max(dict1,key=dict1.get))


# PALINDROME NUMBERS WITH IN A RANGE
# list1=[]
# for num in list(range(10,51))+list(range(100,501)):
#     temp=num
#     rev=0
#     while temp!=0:
#         rem=temp%10
#         rev=rev*10+rem
#         temp//=10
#     if num==rev:
#         list1.append(num)
# print(list1)