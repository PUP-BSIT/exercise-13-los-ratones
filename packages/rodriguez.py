def display_user_info():
    NAME = "John Paul O. Rodriguez"
    AGE = 21
    GENDER = "Male"
    HOBBY = "Love to watch anime"
    GOAL = "To become the first millionaire in the family"

    print(f"Hello, {NAME}!")

    while True:
        print("\n* * * * *")
        print("1. My basic information")
        print("2. My aspirations")
        print("3. Reduta - Comment")
        print("4. Campos - Comment")
        print("5. Manicio - Comment")
        print("6. Gonot - Comment")
        print("7. Exit")

        user_choice = int(input("Please Select an Option (0-6): "))

        match user_choice:
            case 1:
                print(f"I'm {AGE} years old.")
                print(f"I'm a {GENDER}.")
                print(f"My hobby is: {HOBBY}")
                input("Press Enter to continue...")
            case 2:
                print(f"My goal: {GOAL}")
                input("Press Enter to continue...")
            case 3:
                print("Reduta: I wish that too!")
                input("Press Enter to continue...")
            case 4:
                print("Campos: That's a great goal!")
                input("Press Enter to continue...")
            case 5:
                print("Manicio: Dream big and work harder!")
                input("Press Enter to continue...")
            case 6:
                print("Gonot: I know you can do that!")
                input("Press Enter to continue...")
            case 7:
                break
            case _:
                print("Invalid option. Please try again.")