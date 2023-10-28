rno=int(input("Enter Roll No. : "))
sname=input("Enter Student Name : ")
s1=int(input("Enter Subject 1 :"))
s2=int(input("Enter Subject 2 :"))
s3=int(input("Enter Subject 3 :"))

total=s1+s2+s3
per=total/3

print("Roll No. :",rno)
print("Student Name :",sname)
print("Total :",total)
print("percentage :",per)

if s1>=40:
    if s2>=40:
        if s3>=40:
            if per>=70:
                print("Distriction")
            elif per>=60:
                print("First Class")
            elif per>=50:
                print("Second Class")
            elif per>=40:
                print("Pass Class")
            else:
                print("Fail")
        else :
            print("You are Fail In Subject 3")
    else :
        print ("You are Fail In Subject 2")
else:
    print("you are fail In Subject 1")
