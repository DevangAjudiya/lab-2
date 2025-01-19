#print largest and the smallest value out of three
a = float(input("enter first  value a = "))
b = float(input("enter second value b = "))
c = float(input("enter first  value c = "))
if a>b:
    if a>c:
        print("the largest value is =",a)
    else:
        print("the largest value is =",c)
else:
    if(b>c):
        print("the largest value is =",b)
    else:
        print("the largest value is =",c)
if a<b:
    if a<c:
        print("the smallest value is =",a)
    else:
        print("the smallest value is =",c)
else:
    if(b<c):
        print("the smallest value is =",b)
    else:
        print("the smallest value is =",c)
