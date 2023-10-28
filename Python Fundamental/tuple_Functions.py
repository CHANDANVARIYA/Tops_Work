t=(1,2,1.1,2.2,"python",[10,50,80],True,10,20,30,False)

print(t)
print(t.count(1))    # True=1
print(t.index(0))    # False=0


for i in t:
     print(i)
print(t[5])
t[5].append(100)
print(t)

print(50 in t)
