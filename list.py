#creat empty list
city=[]
print(city)
#declare list
name=["isha","shubham","pranjali"]
print(name)
#swap position of list
n=name[0]
name[0]=name[2]
name[2]=n
print(name)
#print element 1by1
for i in name:
    print(i)
#create nested list
no=[2,3,[1,2,3,4,5],4,5]
print(no)
#access nested element
print(no[2])
print(no[2][2])
print(no.append([345,5,4,8]))
print(no)
print(no.extend([88,99,444]))
print(no)


