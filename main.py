import math

def pisagor1(a,b):
    result=math.sqrt((a**2)+(b**2))
    return result

def pisagor2():
    a=int(input("Enter the a edge: "))
    b=int(input("Enter the b edge: "))
    a=float(a)
    b=float(b)

    result=math.sqrt((a**2)+(b**2))
    return result

def pisagor3():
    a=int(input("Enter the a edge: "))
    b=int(input("Enter the b edge: "))
    a=float(a)
    b=float(b)

    result=math.sqrt((a**2)+(b**2))
    return result

aEdge=int(input("Enter the a edge: "))
bEdge=int(input("Enter the b edge: "))
aEdge=float(aEdge)
bEdge=float(bEdge)

pythagorean1=pisagor1(aEdge,bEdge)
print(pythagorean1)

pythagorean2=pisagor2()
print(pythagorean2)

pythagorean3=pisagor3()
print(pythagorean3)