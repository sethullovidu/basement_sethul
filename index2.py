



import turtle

option = 1
print("""
1. Input fields
2. Drawing square with turtle
3. Drawing circle with turtle
(-999 to exit)
""")

while option != -999:
    option = int(input("Enter your option: "))

    if option == 1:
        nlist = []
        while True:
            fname = input("Enter your first name (or -999 to stop): ")
            if fname == "-999":
                break
            lname = input("Enter your last name: ")
            age = int(input("Enter your age: "))
            person = {
                'Name': fname + " " + lname,
                'Age': age
            }
            nlist.append(person)
            print(nlist)

    elif option == 2:
        screen = turtle.Screen()
        t = turtle.Turtle()
        for i in range(4):
            t.forward(100)
            t.left(90)
        screen.exitonclick()

    elif option == 3:
        screen = turtle.Screen()
        t = turtle.Turtle()
        t.circle(70)
        screen.exitonclick()

    elif option == -999:
        print("Exiting the program...")

    else:
        print("Invalid option. Please choose 1, 2, or 3.")







