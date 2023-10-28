'''
1. Simple If
'''

a=int(input("Enter A :"))
if a>0:
    print(a,"Is Positive Number")

'''
2. If/else
'''

a=int(input("Enter A :"))
if a>0:
    print(a,"Is Positive Number")
else:
    print(a,"Is Nagative Number")

a=int(input("Enter A :"))
if a%2==0:
        print(a,"Is Even Number")
else:
    print(a,"Is Odd Number")

a=int(input("Enter A :"))
b=int(input("Enter B :"))
if a>b:
        print(a,"Is Max Number")
else:
    print(b,"Is Max Number")

'''
3. Nested if
'''

a=int(input("Enter A:"))
b=int(input("Enter B:"))
c=int(input("Enter C:"))
if a>b:
    if a>c:
        print(a,":Is Max Number")
    else:
        print(c,":Is Max Number")
elif b>c:
        print(b,": Is Max Number")
else:
        print(c,":Is Max Number")
