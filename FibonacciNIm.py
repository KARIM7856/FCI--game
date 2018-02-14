import random


def fibonacciNim():
        Nims = random.randrange(20, 100, 4)
        print("You will start with {} Nims.".format(Nims))
        Player1 = str( input( "Player one, please enter your nickname : "))
        Player2 = str( input( "Player two, please enter your nickname : "))
        while True:
            try:
                Nim_take = int(input ("{}, you begin, how many nims do you want to remove? ".format(Player1)))
            except ValueError:
                print("Please enter a number.")
            else:
                break
        
        while True:
            if Nim_take >= 1 and Nim_take < Nims:
                
                Nims -= Nim_take
                break
            else:
                while True:
                    try:
                        Nim_take = int(input("{}, the number of nims you choose is out of range please re-enter : ".format(Player1)))
                    except ValueError:
                        print("Please enter a number.")
                    else:
                        break
        
        Turn = 1
        
        while True:
            
            Turn = Turn + 1 
            
            if Turn % 2 == 0:
                
                Player = Player2
                otherPlayer = Player1
            else:
                
                Player = Player1
                otherPlayer = Player2
                
            Nim_take_prev = Nim_take
            while True:
                try:
                    Nim_take = int(input("{}, It's your turn there are {} Nims how many do you want to remove? ".format(Player, Nims)))
                except ValueError:
                    print("Please enter a number.")
                else:
                    break
                
            while True:
                if Nim_take < 1:
                    while True:
                        try:
                            Nim_take = int(input("{}, number of Nims to take can't be less than 1. Please re-enter : ".format(Player)))
                        except ValueError:
                            print("Please enter a number.")
                        else:
                            break
                    
                elif Nim_take > 2 * Nim_take_prev:
                    while True:
                        try:
                            Nim_take = int(input("{}, Number of Nims can't be greater double what {} removed. Please re-enter : "
                                                 .format(Player, otherPlayer)))
                        except ValueError:
                            print("Please enter a number.")
                        else:
                            break
                        
                else:
                        
                    Nims -= Nim_take
                    break
                    
            if Nims <= 0:
                break
        
        print("CONGRATULATIONS {} YOU WON!!!!".format(Player))      


def CPU_fibonacciNim():
    
    fibonacci = [1,1,2,3,5,8,13,21,34,55,89]
    Nims = random.randrange(15, 45, 4)
    names = ["Hassan", "Ibrahim", "Mohamed", "David", "Mostafa",
              "Ahmed","Fatma", "Cyborg", "Adel", "Amr",
              "Ali", "Menna", "Khaled", "Robot", "CPU", "Feras",
               "Omar", "Youssef", "Habiba","Atef"]
    
    names_index = random.randrange(0,20)    
    CPU_name = names[names_index]

    print("You are playing against CPU.")
    print("You will start with {} Nims.".format(Nims))
    Player1 = str( input( "Player one, please enter your nickname : "))
    print("CPU: I'm {}.".format(CPU_name))
    
    while True:
        try:
            Nim_take = int(input("{}, it's your turn take nims : ".format(Player1)))
        except ValueError:
            print("Please enter a number.")
        else:
            break
    
    while True:
        
        if Nim_take < 1:
            while True:
                try:
                    Nim_take = int(input("{}, you have to take some. Please re-enter : "))
                except ValueError:
                    print("Please enter a number.")
                else:
                    break
        
        if  Nim_take >= Nims:
            while True:
                try:
           
                    Nim_take = int(input("{}, you can't take all Nims. Please re-enter : "))
                except ValueError:
                    print("Please enter a number.")
                else:
                    break
    
        else:
            
            Nims -= Nim_take
            break
    
    turn = 0
    while True:
        turn = turn + 1
        
        if turn % 2 != 0:
            Player = CPU_name
            Final = Nims
            
            if Nims <= 2 * Nim_take:
                Nim_take = Nims
                Nims -= Nim_take
                print("{}: I will take {} and leave {}".format(CPU_name, Nim_take, Nims))
                break
            
            else:
                
                while True:
                    
                    temp = Final
                    
                    for I in range(0,11):
                        
                        temp = Final
                        if fibonacci[I] >= temp:
                            
                            Final = fibonacci[I-1]
                            Final = temp - Final
                            break
                    
                    if Final in fibonacci and Final <= 2*Nim_take and Nims - Final > 2*Final:
                        
                        Nim_take = Final
                        Nims -= Nim_take
                        break
            
            print("{}: I will take {} and leave {}".format(CPU_name, Nim_take, Nims))
    
        else:
            
            Player = Player1
            Nim_take_prev = Nim_take
            while True:
                try:
                    Nim_take = int(input("{}, It's your turn there are {} Nims how many do you want to remove? ".format(Player, Nims)))
                except ValueError:
                    print("Please enter a number.")
                else:
                    break
            
            while True:
                
                if Nim_take < 1:
                    while True:
                        try:
                            
                            Nim_take = int(input("{}, you have to take some. Please re-enter : ".format(Player)))
                        except ValueError:
                            print("Please enter a number.")
                        else:
                            break
                        
                elif Nim_take > 2 * Nim_take_prev:
                    while True:
                        try:
                            Nim_take = int(input("{}, Number of Nims can't be greater double what {} removed. Please re-enter : ".format(Player, CPU_name)))
                        except ValueError:
                            print("Please enter a number.")
                        else:
                            break
                            
                else:
                            
                    Nims -= Nim_take
                    break
            
        if Nims <= 0:
            break      
    
    if Player == CPU_name:
        print("CPU beated you.")        
    else:
        print("CONGRATULATIONS {} YOU WON!!!".format(Player))
    
    
Decision = 1
print("Welcome to fibonacci Nim!!!")

while Decision == 1:
    while True:
        try:
            index = int(input("(1) For playing against friend.\n(2) For Playing against CPU."))
        except ValueError:
            print("Please enter a number.")
        else:
            break
    
    if index == 1:
       
        fibonacciNim()
        while True:
            try:
                Decision = int(input("(1)Play again\n(Any other number)Quit"))
            except ValueError:
                print("Please enter a number.")
            else:
                break
        print("\n")
    
    elif index == 2:
        
        CPU_fibonacciNim()
        while True:
            try:
                Decision = int(input("(1)Play again\n(Any other number)Quit"))
            except ValueError:
                print("Please enter a number.")
            else:
                break
        print("\n")
    
    else:
       
        print("ezay ya3ny!!! -_-")
        
print("Thank you for playing fibonacciNim")
