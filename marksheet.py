class Academic_year:
    def __init__(self):
        print("\n\tSinhgad Institute,Vadgoan\t")
        print("\tAcademic year :2023-24\n\n")

class details(Academic_year):
    def info(self):
        name=input("Enter the Name :")
        seat_no=input("Enter the Seat no. :")
        self.name=name
        self.seat_no=seat_no

class timetable(details):
    def timetable(self):
        print("\n\t--------------Time Table 2023-24--------------\t")
        print("\nName :",self.name)
        print("Seat_no :",self.seat_no)
        print("\n\t\tdate\t\ttime\t\tsubcode\t\tsub\t")
        print("\n\t\t9-8-24\t\t4-5pm\t\t101\t\t\tdbms\t")
        print("\t\t10-8-24\t\t4-5pm\t\t102\t\t\tm-2\t")
        print("\t\t11-8-24\t\t4-5pm\t\t103\t\t\tpython\t")
        print("\t\t12-8-24\t\t4-5pm\t\t104\t\t\tjava\t")

class report(timetable):
    def marks(self):
        print("\n\tmarks obtain per subject \t\t")
        d=int(input("DBMS :"))
        m= int(input("M-2 :"))
        p =int( input("PYTHON:"))
        j =int( input("JAVA :"))

        self.d=d
        self.m=m
        self.p=p
        self.j=j

class result(report):
    def card(self):
        print("\t\t------ Report Card ------\t")
        print("\t\tsub code\t\tsub\t\tcrd\t\tgrd\t\tgp\n")
        print("\t\t101\t\t\t\tDBMS\t9\t\tA++\t\t29\n")
        print("\t\t102\t\t\t\tM-2\t\t9\t\tA+\t\t29\n")
        print("\t\t101\t\t\t\tPYTHON\t9\t\tA++\t\t29\n")
        print("\t\t101\t\t\t\tJAVA\t9\t\tA+\t\t29\n")

    def calculation(self):
        total=self.d+self.j+self.p+self.m
        avg=total/4
        if avg >= 90:
            print("GRADE A++")
        elif avg >= 80 and avg < 90:
            print("GRADE A")
        elif avg >= 60 and avg < 80:
            print("GRADE B")
        elif avg >= 35 and avg < 60:
            print("GRADE C")
        else:
            print("FAIL!!!")

r=result()
r.info()
r.timetable()
r.marks()
r.card()
r.calculation()




