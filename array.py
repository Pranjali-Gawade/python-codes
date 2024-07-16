import array
var=array.array('i',[2,3,4,5,6])
print(var)
#index representation
print(var[0])
for i in var:
    print(i)
#add and delete element
var.append(23)
print(var)

del var[-1]
print(var)
#seach the element(odd-even)
for i in var:
    if i%2==0:
        print("Even")
    else:
        print("Odd")