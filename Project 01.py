import random
c = 0
print('''
Welcome to the Game
Here you roll a dice and compete with the computer''')
print("Enter a number between 1 to 6")
print()
while True:
    b = random.randint(1, 6)
    if c == 0:
        a = input("User🙂: ")
    elif 1 <= c <= 5:
        a = input("User😁: ")
    else:
        a = input("User🤩: ")
    try:
        if a == "exit" or a == "e":
            print(f"Your score is {c}")
            print()
            print("Thank you for playing the Game😊👍")
            print()
            break
        elif int(a) > 6 or int(a) < 1:
            print("Enter a number between \"1 to 6\"")
            continue
        elif int(a)>=1 and int(a) <= 6:
            print(f"Computer🖥️🎲: {b}")
            print()
            if int(a) + 2 == b or int(a) - 2 == b:
                print("Than was the neighbour number")
            elif int(a) + 1 == b or int(a) -1 == b:
                print("You are so close try again")
            elif int(a) == b:
                print("💥🎉Yay you did it right🎉💥")
                c += 1
                print(f"Your score is {c}")
            else:
                print("Try again🤕")
            print()
    except ValueError:
        print("Enter a number")