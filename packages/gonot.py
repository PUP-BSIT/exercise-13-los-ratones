def display_user_info():
    age = 20
    name = "Jedi Duncan Gonot"
    aspirations = "To be happy someday"
    town = "Taguig City"
    
    print(f"Hello!, Im {name}")
    
    while True:
        print("\n1. My basic information"
              "\n2. My aspirations",
              "\n3. Reduta - Comment",
              "\n4. Campos - Comment",
              "\n5. Manicio - Comment",
              "\n6. Rodriguez - Comment",
              "\n7. Exit")
        
        user_choice = int(input("Please Select an Option (1-7): "))
        
        match user_choice:
            case 1:
                print(f"Im {age} years old, I live in {town}!")
                input("Press Enter to continue...")
            case 2:
                print(f"My aspiration is {aspirations}.")
                input("Press Enter to continue...")
            case 3:
                print("Reduta: I wish that too!")
                input("Press Enter to continue...")
            case 4:
                print("Campos: I wish you all the best!")
                input("Press Enter to continue...")
            case 5:
                print("Manicio: You're on the right path!")
                input("Press Enter to continue...")
            case 6:
                print("Rodriguez: Don’t give up — you can make it!")
                input("Press Enter to continue...")
            case 7:
                break