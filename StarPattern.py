#1.square pattern
n=5
for i in range(5):
    for j in range(5):
        print("*",end="  ")
    print()


print()
print()
#2.Increasing pattern
n=5
for i in range(5):
    for j in range(i+1):
        print("*",end=" ")
    print()

print()
print()
#3.decreasing pattern
n=5
for i in range(5):
    for j in range(n-i):
        print("*",end=" ")
    print()

print()
print()
#4.right traingle
n=5
for i in range(5):
    for j in range(n-i):
        print(" ",end=" ")
    for j in range(i+1):
        print("*",end=" ")
    print()

print()
print()
#5.left traingle.
n=5
for i in range(5):
    for j in range(i+1):
        print(" ",end=" ")
    for j in range(n-i):
        print("*",end=" ")
    print()


print()
print()
#6.hill pattern
n=5
for i in range(5):
    for j in range(n-i):
        print(" ",end=" ")
    for j in range(i):
        print("*",end=" ")
    for j in range(i+1):
        print("*",end=" ")
    print()


print()
print()
#7.reverse hill
n=5
for i in range(5):
    for j in range(i+1):
        print(" ",end=" ")
    for j in range(i,n-1):
        print("*",end=" ")
    for j in range(n-i):
        print("*",end=" ")
    print()


print()
print()
#8.diamond pattern
n=5
for i in range(n-1):
    for j in range(n-i):
        print(" ",end=" ")
    for j in range(i):
        print("*",end=" ")
    for j in range(i+1):
        print("*",end=" ")
    print()
for i in range(5):
    for j in range(i+1):
        print(" ",end=" ")
    for j in range(i,n-1):
        print("*",end=" ")
    for j in range(n-i):
        print("*",end=" ")
    print()


#9.pyramid pattern increasing
n=5
for i in range(5):
    for j in range(i,n):
        print("",end=" ")
    for j in range(i+1):
        print("*",end=" ")
    print()

print()
print()
#10.pyramid pattern downward.
n=5
for i in range(5):
    for j in range(i+1):
        print("",end=" ")
    for j in range(i,n):
        print("*",end=" ")
    print()

print()
print()

#11.pyramid diamond pattern
n=5
for i in range(n-1):
    for j in range(i,n):
        print("",end=" ")
    for j in range(i+1):
        print("*",end=" ")
    print()
n=5
for i in range(5):
    for j in range(i+1):
        print("",end=" ")
    for j in range(i,n):
        print("*",end=" ")
    print()
