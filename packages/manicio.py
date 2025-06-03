def display_user_info():
    AGE = 20
    NAME = "Dion Kylo C Manicio"
    ASPIRATION = "To become successful in Cybersecurity field."
    TOWN = "Taguig City"
    
    print(f"Hello!, Im {NAME}")
    
    while True:
        print("\n1. My basic information"
              "\n2. My aspirations",
              "\n3. Reduta - Comment",
              "\n4. Campos - Comment",
              "\n5. Gonot - Comment",
              "\n6. Rodriguez - Comment",
              "\n7. Exit")
        
        user_choice = int(input("Please Select an Option (1-7): "))
        
        match user_choice:
            case 1:
                print(f"Im {AGE} years old, I live in {TOWN}!")
                input("Press Enter to continue...")
            case 2:
                print(f"My aspiration is {ASPIRATION}.")
                input("Press Enter to continue...")
            case 3:
                print("Reduta: I wish that too!")
                input("Press Enter to continue...")
            case 4:
                print("Campos: I am considering the same path!")
                input("Press Enter to continue...")
            case 5:
                print("Gonot: I love that!")
                input("Press Enter to continue...")
            case 6:
                print("Rodriguez: Don’t give up — you can make it!")
                input("Press Enter to continue...")
            case 7:
                break