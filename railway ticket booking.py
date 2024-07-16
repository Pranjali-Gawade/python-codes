
import calendar
class railway:
    def __init__(self):
        print("\t\t\tIndian Railway\t\t\t")
        print("\t\tpunctual|safe|security\t\t")
    def route(self):
        r=int(input("\t1. pune -mumbai-pune\n\t2.pune-banglore-pune\n\t3.pune-tirupati-pune\n Enter the route you want"))
        if r==1:
            print("you choose pune-mumbai-pune")
        elif r==2:
            print("you choose pune-banglore-pune")
        elif r==3:
            print("you choose pune-tirupati-pune")
        else:
            print("Something went wrong :(")
class custmor:
    def cust(self):

        name=input("Enter your name : ")
        age=int(input("Enter your age :"))
        no=int(input("Enter your contact number "))
        add=input("Enter the address ")
        y = int(input("Enter year: "))
        m = int(input("Enter month: "))
        print(calendar.month(y, m))

        self.name=name
        self.age=age
        self.no=no
        self.add=add
        self.y=y
        self.m=m
       # self.d=d
class booking(custmor,railway):
    def book_ticket(self):

        comp=int(input("Enter the class you want\n1.local\n2.general\n3.AC\n"))
        if comp==1:
            print("you select local class compartment ")
            tic = int(input("Enter the number of ticket you want :"))
            total=200*tic
            print("your total price is :",total)
        elif comp==2:
            print("you select general compartment ")
            tic = int(input("Enter the number of ticket you want :"))
            total = 500 * tic
            print("your total price is :", total)
        elif comp==3:
            print("you select AC class ")
            tic = int(input("Enter the number of ticket you want :"))
            total = 1000 * tic
            print("your total price is :", total)
        else:
            print("INVALID")

        self.comp=comp
        self.tic=tic
        self.total=total

    def ticket(self):
        print("\t\t\tIndian Railway\t\t\t")
        print("\t\tpunctual|safe|security\t\t")
        print("Booking date :",self.m,self.y)
        print("\t\t\tCustomer Details\t\t\t")
        print("customer name :",self.name)
        print("Customer age :",self.age)
        print("Contact number :",self.no)
        print("Custmer address",self.add)
        print("\t\t\tticket Details\t\t\t")
        print("Class is :",self.comp)
        print("Number of tickets ",self.tic)
        print("Total amount paid :",self.total)


b=booking()
b.route()
b.cust()
b.book_ticket()
b.ticket()









