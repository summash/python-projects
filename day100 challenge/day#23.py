l=[1,2,3,4,5,1,2,1]
l.append(9)
l.sort()
l.sort(reverse=True)
print(l.index(2))
print(l.count(1))
m=l
m[0]=0
print(l)
m=l.copy()
print(l)
l.insert(1, "hiiii!")
x=[1000,2000,3000,4000]
l.extend(x)
print(l)
k=l+m+x#another way of concatination
