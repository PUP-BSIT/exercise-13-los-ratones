from packages import reduta
from packages import campos
from packages import manicio
from packages import rodriguez

while True:
    print("Welcome to Los Ratones!!"
          "\n1. About Kenji Enishi Campos",
          "\n2. ",
          "\n3. About Dion Kylo C Manicio",
          "\n4. About Paul Benidict Reduta",
          "\n5. About John Paul Rodriguez",
          "\n6. Exit"),
    
    user_choice = int(input("Please Select an Option (1-6): "))
    
    match user_choice:
        case 1:
            campos.display_user_info()
            input()
            pass
        case 2:
            #TODO(Jedi Duncan Gonot): Implement the functionality for option 2
            pass
        case 3:
            manicio.display_user_info()
            input()
        case 4:
            reduta.display_user_info()
            input()
        case 5:
            rodriguez.display_user_info()
            input()
        case 6:
            exit()
        
        case _:
            print("Invalid Option. Please try again.")
            
