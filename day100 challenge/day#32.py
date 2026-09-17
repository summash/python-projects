a={1,2,3,4,6,5}
b={6,5,7,8,9}
b1={1,2,"hiiii"}
c={"yaisa"}
print(a.union(b))
print(a.update(b))
print(a.intersection(b))
print(a.symmetric_difference(b))#a U b - a intertsection b
print(a.isdisjoint(c))#checks if they are disjoint
print(a.issuperset(b))#
print(b1.issubset(a))
print(a.add("hii"))
#print(b.update(1,2,3,4,"hiii"))
print(a.remove(1))#shows error if the item id not present
print(a.discard(91))#will not show error
print(b.pop())
del (b)
print(a.clear())
if 1 in a:
    print("yes")
else:
    print("no")




