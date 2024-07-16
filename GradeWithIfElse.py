m1=int(input("Enter the marks m1 : "))
m2=int(input("Enter the marks m2 :"))
m3=int(input("Enter the marks m3 :"))
total=m1+m2+m3
avg=total/3
print("Total :",total)
print("Average :",avg)
if avg>=90:
    print("GRADE A++")
elif avg>=80 and avg<90:
    print("GRADE A")
elif avg>=60 and avg<80:
    print("GRADE B")
elif avg>=35 and avg<60:
    print("GRADE C")
else:
    print("FAIL!!!")
