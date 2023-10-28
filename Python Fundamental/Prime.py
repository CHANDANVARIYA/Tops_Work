n=int(input("Enter no.: "))

if n%2!=0:
    for i in (3,int(n/2)+1,2):
        if n%i==0:
            print (n,"Is not Prime Number")
            break
    else:
        print (n,"Is Prime Number")
else:
    print (n,"is not Prime Number ")

'''
n%2==0 = Even Right,odd Wrong
n%2!=0 = odd Right, Even Wrong
'''

