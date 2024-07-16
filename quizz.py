py=input("Do u want to play python quiz ?")
score=0
if py.lower()=="yes":
    print("Let's play quizz😁👍")
    que1=input("1. Who developed Python Programming Language?\na) Wick van Rossum\nb) Rasmus Lerdorf\nc) Guido van Rossum\nd) Niene Stom\n")
    if que1.lower()=="c":
        print("Correct✌️")
        score+=1
    else:
        print("Wrong😑")


    que2= input("2. Which type of Programming does Python support?\n a) object-oriented programming\nb) structured programming\nc) functional programming\nd) all of the mentioned\n")
    if que2.lower() == "d":
        print("Correct✌️")
        score += 1
    else:
        print("Wrong😑")

    que3 = input("3. Is Python case sensitive when dealing with identifiers?\na) no\nb) yes\nc) machine dependent\nd) none of the mentioned\n")
    if que3.lower() == "b":
        print("Correct✌️")
        score += 1
    else:
        print("Wrong😑")

    que4 = input("4. Which of the following is the correct extension of the Python file?\na) .python\nb) .pl\nc) .py\nd) .p\n")
    if que4.lower() == "c":
        print("Correct✌️")
        score += 1
    else:
        print("Wrong😑")

    que5 = input("5. Is Python code compiled or interpreted?\na) Python code is both compiled and interpreted\nb) Python code is neither compiled nor interpreted\nc) Python code is only compiled\nd) Python code is only interpreted\n")
    if que5.lower() == "a":
        print("Correct✌️")
        score += 1
    else:
        print("Wrong😑")

    que6 = input("6.All keywords in Python are in _________\na) Capitalized\nb) lower case\nc) UPPER CASE\nd) None of the mentioned\n")
    if que6.lower() == "d":
        print("Correct✌️")
        score += 1
    else:
        print("Wrong😑")

    que7 = input("7.What will be the value of the following Python expression?\t4 + 3 % 5\na) 7\nb) 2\nc) 4\nd) 1\n")
    if que7.lower() == "a":
        print("Correct✌️")
        score += 1
    else:
        print("Wrong😑")

    que8 = input("8.Which of the following is used to define a block of code in Python language?\na)Indentation\nb) Key\nc) Brackets\nd) All of the mentioned\n")
    if que8.lower() == "a":
        print("Correct✌️")
        score += 1
    else:
        print("Wrong😑")

    que9 = input("9.Which keyword is used for function in Python language?\na) Function\nb) def\nc) Fun\nd) Define\n")
    if que9.lower() == "b":
        print("Correct✌️")
        score += 1
    else:
        print("Wrong😑")

    que10= input("10. Which of the following character is used to give single-line comments in Python?\na) //\nb) #\nc) !\nd) /*\n")
    if que10.lower() == "b":
        print("Correct✌️")
        score += 1
    else:
        print("Wrong😑")

else:
    print("okay, No problem😒")
    quit()

print("You got "+str(score)+" Quetion correct 🎉")
print("You got "+str((score/10)*100)+"%")
avg=((score/10)*100)

if avg>=90:
    print("Awesome!!")
elif avg>=60 and avg<90:
    print("Very Good!!")
elif avg>=30 and avg<60:
    print("Not Bad")
else:
    print("U have to work on that :(")

