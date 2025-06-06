def display_user_info():
    age = 20
    name = "Kenji Enishi Campos"
    aspirations = "To become a successful individual that can help my family"
    town = "Taguig City"
    
    print(f"Hello!, Im {name}")
    
    while True:
        print("\n1. My basic information"
              "\n2. My aspirations",
              "\n3. Reduta - Comment",
              "\n4. Manicio - Comment",
              "\n5. Gonot - Comment",
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
                print("Reduta: Wow, you can do it!")
                input("Press Enter to continue...")
            case 4:
                print("Manicio: Keep pushing forward!")
                input("Press Enter to continue...")
            case 5:
                print("Gonot: Keep going my friend!")
                input("Press Enter to continue...")
            case 6:
                print("Rodriguez: Don’t give up — you can make it!")
                input("Press Enter to continue...")
            case 7:
                break