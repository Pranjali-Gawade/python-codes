class product():
    def __init__(self):
        name=input("Enter the product name :")
        comp=input("Enter the brand of product")
        material=input("Enter the material of the product :")
        colour=input("Enter the colour of the product :")
        size=input("Enter the size of the product :")

        self.name=name
        self.material=material
        self.comp=comp
        self.colour = colour
        self.size=size

    def customerDetails(self):
        cname=input("Enter customer name :")
        add=input("Enter Address :")
        cont=input("Enter contact no. :")

        self.cname=cname
        self.add=add
        self.cont= cont

    def discount(self):
        Sprice=int(input("Enter the selling price :"))
        Oprice=int(input("Enter the original price :"))

        print("The discount price you got: ",Sprice-Oprice)

    def Bill(self):
        print("\n\n\t\t4Dimensions\n\n")
        print("Customer name: ",self.cname)
        print("Adrress: ",self.add)
        print("Contact: ",self.cont)

        print("\n\tProduct: ")
        print("Name: ",self.name)
        print("Brand: ",self.comp)
        print("Material: ",self.material)
        print("Size: ",self.size)
        print("Colour: ",self.colour)


p = product()
p.customerDetails()
p.Bill()
p.discount()
