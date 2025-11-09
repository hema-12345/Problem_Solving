print("pattern-1")
n=5
p=1
for i in range(n):
    for j in range(n):
        print(chr(64+p),end=" ")
        p+=1
    print()
print()

print("pattern-2")
n=5
p=1
for i in range(n):
    for j in range(i+1):
        print(chr(64+p),end=" ")
    p+=1
    print()

print()

print("pattern-3")
n=5
for i in range(n):
    p=1
    for j in range(i+1):
        print(chr(64+p),end=" ")
        p+=1
    print()

print()

print("pattern-4")
n=5
for i in range(n):
    p=1
    for j in range(n-i):
        print(chr(64+p),end=" ")
        p+=1
    print()


print()
print("pattern-5")
n=5
for i in range(n):
    p=1
    for j in range(n-i):
        print(" ",end=" ")
    for j in range(i+1):
        print(chr(64+p),end=" ")
        p+=1
    print()

print()
print("pattern-6")
n=5
for i in range(n):
    p=1
    for j in range(i+1):
        print(" ",end=" ")
    for j in range(n-i):
        print(chr(64+p),end=" ")
        p+=1
    print()

print()
print("pattern-7")
n=5
for i in range(5):
    p=1
    for j in range(n-i):
        print(" ",end=" ")
    for j in range(i):
        print(chr(64+p),end=" ")
        p+=1
    for j in range(i+1):
        print(chr(64+p),end=" ")
        p+=1
    print()

print()
print("pattern-8")
n=5
for i in range(5):
    p=1
    for j in range(n-i):
        print(" ",end=" ")
    for j in range(i):
        print(chr(64+p),end=" ")
        p+=1
    for j in range(i+1):
        print(chr(64+p),end=" ")
        p-=1
    print()

print()
print("pattern-9")
n=5
for i in range(5):
    p=1
    for j in range(i+1):
        print(" ",end=" ")
    for j in range(i,n-1):
        print(chr(64+p),end=" ")
        p+=1
    for j in range(n-i):
        print(chr(64+p),end=" ")
        p+=1
    print()

print()
print("pattern-10")
n=5
for i in range(5):
    p=1
    for j in range(i+1):
        print(" ",end=" ")
    for j in range(i,n-1):
        print(chr(64+p),end=" ")
        p+=1
    for j in range(n-i):
        print(chr(64+p),end=" ")
        p-=1
    print()


print()
print("pattern-11")
"""DIAMOND PATTERN"""
n=5
for i in range(n-1):
    p=1
    for j in range(n-i):
        print(" ",end=" ")
    for j in range(i):
        print(chr(64+p),end=" ")
        p+=1
    for j in range(i+1):
        print(chr(64+p),end=" ")
        p+=1
    print()
for i in range(5):
    p=1
    for j in range(i+1):
        print(" ",end=" ")
    for j in range(i,n-1):
        print(chr(64+p),end=" ")
        p+=1
    for j in range(n-i):
        print(chr(64+p),end=" ")
        p+=1
    print()


print()
print("pattern-12")
"""----DIAMOND PATTERN-----"""
n=5
for i in range(n-1):
    p=1
    for j in range(n-i):
        print(" ",end=" ")
    for j in range(i):
        print(chr(64+p),end=" ")
        p+=1
    for j in range(i+1):
        print(chr(64+p),end=" ")
        p-=1
    print()
for i in range(n):
    p=1
    for j in range(i+1):
        print(" ",end=" ")
    for j in range(i,n-1):
        print(chr(64+p),end=" ")
        p+=1
    for j in range(n-i):
        print(chr(64+p),end=" ")
        p-=1
    print()

