#check the three point are fall in the same line
print("enter first point")
x1=float(input("enter x1 = "))
y1=float(input("enter y1 = "))
print("enter second point")
x2=float(input("enter x2 = "))
y2=float(input("enter y2 = "))
print("enter third point")
x3=float(input("enter x3 = "))
y3=float(input("enter y3 = "))
area = (x1*(y2-y3)+x2*(y3-y1)+x3*(y1-y2))/2
if(area==0):
    print("all point are in one line")
else:
    print("all points are in difrent line")
