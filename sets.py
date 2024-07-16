set={ 1,2,3,'w',"tt"}
print(set)
#add new element
set.add(33)
print(set)
set.update({34,45,67})
print(set)
#deletion
set.remove(67)
print(set)
set.discard(34)
print(set)
#delet entire set
#del(set)
#print(set)
#union operation
p={1,2,3,4,5}
s={4,5,6,7,8}
print("Union :",p|s)
#intersection
print("Intersection :",p&s)
#symetric differance
print("Symetric difference :",p^s)
#difference
print("Diference :",p-s)
print("Difference :",s-p)
