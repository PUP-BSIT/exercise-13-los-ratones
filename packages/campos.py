def display_user_info():

    age = 20
    name = "Kenji Enishi Campos"
    aspirations = "To become a successful individual that can help my family"
    town = "Taguig City"
    
    print(f"Hello!, Im {name}")
    
    while True:
        print("\n1. My basic information"
              + "\n2. My aspirations"
              + "\n3. Reduta - Comment"
              + "\n4. "
              + "\n5. "
              + "\n6. "
              + "\n7. Exit")
        
        user_choice = int(input("Please Select an Option (1-7): "))
        
        match user_choice:
            case 1:
                print(f"Im {age} years old, I live in {town}!")
                input()
            case 2:
                print(f"My aspiration is {aspirations}.")
                input()
            case 3:
                print("Reduta: Wow, you can do it!")
                input()
            case 4:
                pass
            case 5:
                pass
            case 6:
                pass
            case 7:
                break