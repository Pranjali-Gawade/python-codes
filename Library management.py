class name:
    def __init__(self):
        print("\t\tSinhgad Library\t\t")
        print("\tFE|TE|SE|BE|BSC|BCA|DIP\t\n")

    def options(self):
        while True :
            num=int(input("1.Add book details\n2.Display book\n3.list the total number of book\n4.exit\nEnter the no.which u want :"))
            score=0
            if num==1:
                bname=input("Enter the book name :")
                aname=input("Enter the Author name :")
                page=int(input("Enter the pages of book :"))
                price=int(input("Enter the price of book :"))
                score+=1
                self.bname=bname
                self.aname=aname
                self.page=page
                self.price=price
                self.score=score

            elif num==2:
                print("Book name :",self.bname)
                print("Author name :",self.aname)
                print("Pages :",self.page)
                print("Price :",self.price)

            elif num==3:
                print("Total no. of books avalaible",self.score)

            elif num==4:
                exit()
            else:
                print("INVALID")

n=name()
n.options()





