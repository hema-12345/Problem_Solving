# n=5
# for i in range(n):
#     for j in range(n):
#         if ( i==0 or i==n-1 or j==0 or j==n-1):
#             print('*',end=" ")
#         else:
#             print(' ',end=" ")
#     print()

# n=5
# for i in range(n):
#     for j in range(n):
#         if  i==0 or i==n-1 or j==0 or j==n-1 or i==n//2 or j== n//2:
#             print("*",end=" ")
#         else:
#             print( " ",end=" ")
#     print()

# n=5
# for i in range(n):
#     for j in range(n):
#         if  i==n//2 or j== n//2:
#             print("*",end=" ")
#         else:
#             print( " ",end=" ")
#     print()

# n=5
# for i in range(n):
#     for j in range(n):
#         if  i==j or i+j==n-1 or i==0 or i== n-1:
#             print("*",end=" ")
#         else:
#             print( " ",end=" ")
#     print()

# n=5
# for i in range(n):
#     for j in range(i+1):
#         if  j==0 or i==j or i==n-1:
#             print("*",end=" ")
#         else:
#             print( " ",end=" ")
#     print()

# n=5
# for i in range(n):
#     for j in range(n-i):
#         if j==0 or i==0 or i+j==n-1 :
#             print("*",end=" ")
#         else:
#             print( " ",end=" ")
#     print(end=" ")
#     for j in range(i+1):
#         print(" ",end=" ")
#     for j in range(n-i):
#         if  i==0  or j==n-i-1 or j==0:
#             print("*",end=" ")
#         else:
#             print( " ",end=" ")
#     print()


# n=5
# for i in range(n):
#     for j in range(n-i):
#         print(" ",end=" ")
#     for j in range(i+1):
#         if  i==n-1 or j==n-1 or i+j==n-1:
#             print("*",end=" ")
#         else:
#             print( " ",end=" ")
#     print()


print("PRINTING MY NAME USING PATTERNS")
n=5
for i in range(n):
    for j in range(n):
        if i==n//2 or j==0 or j==n-1:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print(end=" ")
    for j in range(n):
        if i==0 or i==n-1 or i==n//2 or j==0:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print(end=" ")
    for j in range(n):
        if j==0 or j==n-1 or i==j in (1,2) or (i==1 and j==3):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print(end=" ")
    for j in range(n):
        if i==n//2 or (i==0 and j==2) or (i==1 and j in (1,3) or (j==0 and 1<i<=4) or j==n-1 and  1<i<=4):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()