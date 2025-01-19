#find the point is on the circle ,outside the circle,inside the circle.
import math
r=float(input("enter the redius"))
print("enter the center of the circle")
x1=float(input("enter the x cordinet = "))
y1=float(input("enter the y cordinet = "))
print("enter the point")
x2=float(input("enter the x cordinet = "))
y2=float(input("enter the y cordinet = "))
dis=(x1-x2)**2 + (y1-y2)**2
distanc = math.sqrt(dis)
if(r==distanc):
    print("on the circle")
elif(r<distanc):
    print("inside the circle")
else:
    print("outside the circle")
