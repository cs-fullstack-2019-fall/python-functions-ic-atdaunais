def main():
    favoriteTeacher = "Kevin"
    problem1(favoriteTeacher)
    problem2()
    sumOf3Numbers(50, 2, 8)
    problem4("Andrew")


def problem1(input1):
    print(input1)


def problem2():
    userInput = ""
    while userInput != "q":
        userInput = input("Enter anything. Press 'q' to quit: ")
        if userInput == "q":
            print("Goodbye")


def sumOf3Numbers(number1, number2, number3):
    total = number1 + number2 + number3
    print(total)


def problem4(name):
    userAmount = int(input("How many times would you like the message to print? "))
    for x in range (0, userAmount, 1):
        print(f"Hello {name}")


main()