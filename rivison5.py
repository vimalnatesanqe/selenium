def fun(a):
    print(a)
fun("vimal")

def fun1(b):
    return b
x=fun1("return value is 35")
print(x)

######list as argument

def fun2(list):
    print(list)
    list.append(11)
    return list
a=[1,2,3,4,5,6,7,8]
x=fun2(a)
print(x)

def fun3(a,b,c,*args):
    print(a,b,c)
    for i in args:
        print(i)
lis=[1,2,3,4,5,6,7,[8,9]]
fun3(*lis)


def fun4(a,b,c,*args):
    print(a,b,c,args)
set={1,2,3,4,5,6,7}
fun4(*set)

def fun5(dict):
    print(dict)
    for key,value in dict.items():
        print(f"key is {key} and value is{value}")
dict={"name":"vimal","age":35,"location":"NKL"}
fun5(dict)

def fun6(name,age,location):
    print(name,age,location)
dict={"name":"vimal","age":35,"location":"NKL"}
fun6(**dict)

def fun7(**args):
    print(args)
    for i in args.items():
        print(i)
dict={"name":"vimal","age":35,"location":"NKL"}
fun7(**dict)