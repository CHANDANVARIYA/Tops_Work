l=[1,2,1.1,2.2,"tops",True,1,2,10,"python",False]

print(l)
print(len(l))

l.append(100)  # append means add in last#
print(l)

l1=l.copy()  # copy karva thi darek next answer is effect nathi avti#
print(l1)

l1.append(200)
print(l1)

l2=l         #l2=l , l=l2 aevu samji ne next darek answer par effect karse#
print(l2)

l2.append(300)
print(l2)

print(l.count(1))

l3=[1000,2000,3000]
l.extend(l3)
print(l)

print(l.index(10))

l.insert(5,1001)
print(l)

l.pop()
print(l)

l.remove(10)
print(l)

l.reverse()
print(l)

for i in l:
    print(i)

print(1001 in l)
