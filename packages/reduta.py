def display_user_info():
    
    AGE = 20
    NAME = "Paul Benidict Reduta"
    ASPIRATION = "To become a successful software engineer"
    TOWN = "Taguig City"
    
    print(f"Hello!, Im {NAME}")
    
    while True:
        print("\n1. My basic information"
              "\n2. My aspirations",
              "\n3. Campos - Comment",
              "\n4. Manicio - Comment",
              "\n5. Gonot - Comment",
              "\n6. Rodriguez - Comment",
              "\n7. Exit")
        
        user_choice = int(input("Please Select an Option (1-7): "))
        
        match user_choice:
            case 1:
                print(f"Im {AGE} years old, I live in {TOWN}!")
                input()
            case 2:
                print(f"My aspiration is {ASPIRATION}.")
                input()
            case 3:
                print("Campos: WOW! you live in Taguig City too!")
                input()
            case 4:
                print("Manicio: you'll get there!")
                input()
            case 5:
                print("Gonot: Continue on your journey!")
                input()
            case 6:
                print("Rodriguez: Don’t give up — you can make it!")
                input()
            case 7:
                break