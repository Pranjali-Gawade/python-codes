num1=int(input("Enter the number 1 : "))
num2=int(input("Enter the number 2 : "))
op=input("Enter the operator :")
match op:
    case "+":
        print("Addition is :",num1+num2)
    case "-":
        print("Substraction  is :", num1-num2)
    case "*":
        print("Multiplication is :", num1*num2)
    case "/":
        print("Division is :", num1/num2)
    case "%":
        print("Reminder is :", num1%num2)
    case _:
        print("*** INVALID OPERATOR ***")