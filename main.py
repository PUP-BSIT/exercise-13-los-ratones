while True:
    print("Welcome to Los Ratones!!"
          + "\n1. "
          + "\n2. "
          + "\n3. "
          + "\n4. "
          + "\n5. "
          + "\n6. Exit")
    
    user_choice = int(input("Please Select an Option (1-6): "))
    
    match user_choice:
        case 1:
            #TODO(Kenji Enishi Campos): Implement the functionality for option 1
            pass
        case 2:
            #TODO(Jedi Duncan Gonot): Implement the functionality for option 2
            pass
        case 3:
            #TODO(Dion Manicio): Implement the functionality for option 3
            pass
        case 4:
            #TODO(Paul Benidict Reduta): Implement the functionality for option 4
            pass
        case 5:
            #TODO(John Paul Rodriguez): Implement the functionality for option 5
            pass
        case 6:
            exit()
        case _:
            print("Invalid Option. Please try again.")
            
