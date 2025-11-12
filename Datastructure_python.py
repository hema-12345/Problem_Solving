#list data_structure
list=[1,2,3,4,5]
#append=it is used to add element into a list at last.
list.append(6)
print(list)
#insert=it is used to add element at particular position
list.insert(2,2.5)
print(list)
#extend=
list.extend([7,8,6,78,0])
print(list)
#remove
list.remove(2.5) #pass value to remove.
print(list)
#pop()
list.pop(6)
print(list)
list.insert(6,7)
print(list)
list.pop()
print(list)
#clear
list.clear()
print(list)
print(min(list))
print(max(list))
list.sort()
print(list)
list.reverse()
print(list)
arr1=[3,5,6,7,2,5,6]
arr1.append(arr1)
print(arr1)
arr1=[3,5,6,7,2,5,6]
arr1.extend(arr1)
print(arr1)
#Deepcopy
list1=[2,3,4,5,6]
list2=list1
list2.append(56)
print(list2)
print(list1)
#Shallow copy
list1.copy(list2)
list2.append(67)
print(list1)
print(list2)



#tuple datastructure
arr=(1,)
arr1=(3,5,6,7,2,5,6)
print(len(arr1))
print(arr1+arr1)
print(max(arr1))
print(min(arr1))
arr.clear()



#set data structure
set={1,2,3,4,5}
#add=to add an element to a set.
print(set.add(6))
#print(set)
#remove=gives an error
set.remove(5)
print(set)
#discard
set.discard(7)
print(set)
s1={1,2,3,45,6,7,5,4}
s2={6,5,7,89,0}
print(s1.union(s2))
print(s1&s2) #intersection()
print(s1|s2) #union()
print(s1.intersection(s2))

#dictionary data structure
dict1={1:'hema',2:'lakshmi',3:"ankamreddy"}
len(dict1)
print(pop(3))
dict1[3]="dhana"
print(dict1)
dict1.update(dict1)
del dict1[2]
dict1.get(3)
max(dict1,key=dict1.get)