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
        print("3. Comment from Teammate 1")
        print("4. Comment from Teammate 2")
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
                print(f"Teammate 1 says: ")
            case 4:
                print(f"Teammate 2 says: ")
            case 0:
                break
            case _:
                print("Invalid option. Please try again.")