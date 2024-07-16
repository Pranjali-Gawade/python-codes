class bank():
    def __init__(self,name):
        self.name=name

    def fun(self):
        print(self.name)

class HDFC():
    def fun(self):
        return 7.00;

class ICICI():
    def fun(self):
        return 7.45;

class SBI():
    def fun(self):
        return 8.00;

    def calculating(principal,rate,time):
        return (principal*rate*time)/100

c=int(input("Enter the following choice\n1.HDFC\n2.ICICI\n3.SBI\n"))
if c==1:
    bank=HDFC("HDFC")
elif c==2:
    bank=ICICI("ICICI")
elif c==3:
    bank=SBI("SBI")
else:
    print("Invalid choice")
    exit()
principal=float(input("Enter the principal amount: "))
time=float(input("Enter the time (in year)"))









