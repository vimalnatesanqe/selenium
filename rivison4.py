list1=[1,2,3,4,5]
list2=[6,7,8,9,10]

for i in list1:
    print(i)

for i,j in enumerate(list1):
    print(i,j)

for l1,l2 in zip(list1,list2):
    print(l1,l2)

list3=list1+list2
list4=[*list1,*list2]
list5=list1.extend(list2)

print(list3)
print(list4)
print(list5)

# i=0
# while i<=len(list4):
#     print(list4[i])
#     i+=1
    
tup=1,2,3,4,5,6
print(type(tup))  
print(tup)  

for i in tup:
    print(i)
tup1=7,8,9,10
print(tup+tup1)

first,*mid,last=[1,2,3,4,5,6,7]
print(first)
print(mid)
print(last)

print(*tup1,*tup)

set1={1,2,3,4,5,6}
set2={7,7,7,8,9,10}
print(set1.union(set2))
x={*set1,*set2}
print(x)
print(type(x))

dict1={"name":"vimal","age":34}
dict={"location":'NKL'}

print({**dict1,**dict})

for i in dict1:
    print(i)
for j in dict1.values():
    print(j)
