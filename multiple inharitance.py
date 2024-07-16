class Addition:
    def add(self):
        a=int(input("Enter the a :"))
        b=int(input("Enter the b :"))
        return a+b;

class substraction:
    def sub(self):
        a = int(input("Enter the a :"))
        b = int(input("Enter the b :"))
        return a-b;

class multiplication:
    def mul(self):
        a = int(input("Enter the a :"))
        b = int(input("Enter the b :"))
        return a*b;

class division:
    def div(self):
        a = int(input("Enter the a :"))
        b = int(input("Enter the b :"))
        return a / b;

class reminder:
    def rem(self):
        a = int(input("Enter the a :"))
        b = int(input("Enter the b :"))
        return a%b;

class calculation(Addition,substraction,multiplication,division,reminder):
    def __init__(self):
        print(" Welcome to digital calculator")


c=calculation()
while True:
    print("1.addition\t2.substraction\t3.multiplication\t4.division\t5.reminder")
    op = int(input("Enter the operation u want to perform"))
    match op:
        case 1:print("Addition :",c.add())



