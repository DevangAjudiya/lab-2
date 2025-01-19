#exept the marks of three sub
#print total and avrage
#and print student pass or not
name = input("enter the name = ")
print("enter the marks ")
sub1 = float(input("sub1="))
sub2 = float(input("sub2="))
sub3 = float(input("sub3="))
print("the sum ==",sub1+sub2+sub3)
print("the avg ==",(sub1+sub2+sub3)/3)
avg = (sub1+sub2+sub3)/3
if(sub1>=40 and sub2>=40 and sub3>=40):
    if(avg>=40 and avg<=44):print("grade = P")
    elif(avg>44 and avg<=49):print("grade = C")
    elif(avg>49 and avg<=54):print("grade = B")
    elif(avg>54 and avg<=59):print("grade = B+")
    elif(avg>59 and avg<=69):print("grade = A")
    elif(avg>69 and avg<=79):print("grade = A+")
    elif(avg>79 and avg<=100):print("grade = o")
else:
    print("fail \n grade = F ")
    
