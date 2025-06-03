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
        print("0. Exit")

        user_choice = input("Please Select an Option (0-4): ")

        match user_choice:
            case 1:
                print(f"I'm {AGE} years old.")
                print(f"I'm a {GENDER}.")
                print(f"My hobby is: {HOBBY}")
            case 2:
                print(f"My goal: {GOAL}")
            case 3:
                print("Reduta: I wish that too!")
                input()
            case 4:
                print("Campos: That's a great goal!")
                input()
            case 5:
                print("Manicio: Dream big and work harder!")
                input()
            case 0:
                break
            case _:
                print("Invalid option. Please try again.")