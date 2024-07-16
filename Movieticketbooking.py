print("\tWELCOME\t ")
print("1.Royal\n2.Silver\n3.Sofa")
choice=int(input("Enter your choice"))
if choice==1:
    print("price per person :1000")
    ticket=int(input("how many seats you want"))
    total=1000*ticket
    print("Total price is :",total)
    if ticket==1:
        print("your seat no. is AA1")
    elif ticket==2:
        print("your seat no are AA2,AA3")
    elif ticket==3:
        print("your seat no are AA4,AA5,AA6")
    elif ticket==4:
        print("your seat no are AA7,AA8,AA9,AAA")
    else:
        print("Housefull!!!!!!")
elif choice==2:
    print("price per person :500")
    ticket=int(input("how many seats you want"))
    total=500*ticket
    print("Total price is :",total)
    if ticket==1:
        print("your seat no. is AB1")
    elif ticket==2:
        print("your seat no are AB2,AB3")
    elif ticket==3:
        print("your seat no are AB4,AB5,AB6")
    elif ticket==4:
        print("your seat no are AB7,AB8,AB,ABB")
    else:
        print("Housefull!!!!!!")
else:
    print("price per person :100")
    ticket=int(input("how many seats you want"))
    total=100*ticket
    print("Total price is :",total)
    if ticket==1:
        print("your seat no. is BB1")
    elif ticket==2:
        print("your seat no are BB2,BB3")
    elif ticket==3:
        print("your seat no are BB4,BB5,BB6")
    elif ticket==4:
        print("your seat no are BB7,BB8,BB9,BBB")
    else:
        print("Housefull!!!!!!")

#grade,odd,even,positive

