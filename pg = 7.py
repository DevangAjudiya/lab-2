#accept the nuber from the usear,and print the number of digits in it
a = int(input("enter the number = "))
num = 0
while(a>0):
    a=a//10
    num = num +1
print(num)
