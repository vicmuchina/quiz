print("Welcome to computer quiz!")
answer = input("Do you want to do the quiz")
score = 0

if answer.lower() == "yes":
    answer = input("1.What does CPU stand for?")
    if answer.lower() == "central processing unit":
        score += 1
        print("Correct! your score is " + str(score))
    else:
        print("Incorrect!")
    print()

    answer = input("2.What does GPU stand for?")
    if answer.lower() == "graphics processing unit":
        score += 1
        print("Correct! your score is " + str(score) + " out of 10")
    else:
        print("Incorrect!")
    print()

    answer = input("3.What does RAM stand for?")
    if answer.lower() == "random access memory":
        score += 1
        print("Correct! your score is  " + str(score) + " out of 10")
    else:
        print("Incorrect!")
    print()

    answer = input("4.What does ROM stand for?")
    if answer.lower() == "read only memory":
        score += 1
        print("Correct! your score is  " + str(score) + " out of 10")
    else:
        print("Incorrect!")
    print()

    answer = input("5.What does PSU stand for?")
    if answer.lower() == "power supply unit":
        score += 1
        print("Correct! your score is  " + str(score) + " out of 10")
    else:
        print("Incorrect!")
    print()

    answer = input("6.What does HDD stand for?")
    if answer.lower() == "hard disk drive":
        score += 1
        print("Correct! your score is  " + str(score) + " out of 10")
    else:
        print("Incorrect!")
    print()

    answer = input("7.What does SSD stand for?")
    if answer.lower() == "solid state drive":
        score += 1
        print("Correct! your score is  " + str(score) + " out of 10")
    else:
        print("Incorrect!")
    print()

    answer = input("8.What does USB stand for?")
    if answer.lower() == "universal serial bus":
        score += 1
        print("Correct! your score is  " + str(score) + " out of 10")
    else:
        print("Incorrect!")
    print()

    answer = input("9.What does LAN stand for?")
    if answer.lower() == "local area network":
        score += 1
        print("Correct! your score is  " + str(score) + " out of 10")
    else:
        print("Incorrect!")
    print()

    answer = input("10.What does WAN stand for?")
    if answer.lower() == "wide area network":
        score += 1
        print("Correct! your score is  " + str(score) + " out of 10")
    else:
        print("Incorrect!")
    print()

    print("Congratulations! You have completed the quiz!")
else:
    quit()