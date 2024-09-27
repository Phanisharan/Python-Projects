def user(User):

    print('Hey',User,'~~~ Welcome to the Game of Treasure ~~~~')
    Game = input('Do You want to play the Game (Yes/No) : ').lower()
    return Game
    

def game(Game):

    if Game == 'yes':
        print('You are Entered into the Game!!!!....')
        startGame()
    
    elif Game == 'no':
        print('You are exited from the game...')

    else:
        print('You are entered the wrong input ###')
        Game = input('Do You want to play the Game (Yes/No) : ').lower()
        return Game
        

def startGame():

    Move_forward = input('Do you want to continue the game? (Yes/No) : ').lower()

    if Move_forward == 'yes':

        print('''Here is the game. Where you have 4 directions(Right '>' , Left '<', Up '^', Down 'v') and 4 paths \n 1. If you go left you will find a way to the Den.\n 2. If you go right you will find a river.\n 3. If you go Up your path will be towards the Top of the Mountain. \n 4. If you go Down You will Find a black hole.\n There is Treasure hidden from one of the above place.\n Now your goal is to find the Treasure / die and exit from the game. You have only one chance to play and you should only choose one direction.\n Once you choose the direction you need to go forward you cannot come backward. \n If you choose the wrong direction then you may die and you will exit from the game.\n So, Choose Your Path wisely to find the Treasure....\n Here are the directions to choose: \n a. To Move Right Enter 'r'. \n b. To Move Left Enter 'l'. \n c. To Move Up Enter 'u'. \n d. 'To Move Down Enter 'd'. \n If you press WRONG INPUT then you will die and exit from the game.''')

        Move_forward = input('Do you want to continue? (Yes/No) : ').lower()

        if Move_forward == 'yes':

            print(f'Ok! {User} Let\'s play the game!!!...')
            play = input('Choose Your Direction (Left-(l) / Right-(r) / Up-(u) / Down-(d)). If you enter the wrong input you gonna DIE : ').lower()

            if play == 'l':
                l_direction(play)

            elif play == 'r':
                r_direction(play)

            elif play == 'u':
                u_direction(play)

            elif play == 'd':
                d_direction(play)

            else:
                print('You are died and exited from the game....')

        else:
            Exit()

    else:
        Exit()


def l_direction(play):

    if play == 'l':
        print('You are 1km near to the Den.')
        play = input('Do you want to move forward or you want to exit from the game.\n For Move-Forward (Press "m") / Exit (Press "e") : ').lower()

        if play == 'm':
            print("You have reached your destination.")
            play = input('The place is dark do you want to on the light.\n To on the Light (Press "l") / If not (Press "o") : ').lower()

            if play == 'l':
                play = input('Their is a Egypt box. Do you want to open it? (y/n) : ').lower()

                if play == 'y':
                    print('You are killed by the mummy Your are died and exited from the game.')

                else:
                    print('You are exited from the game.')
            else:
                print('You have ended your life in the dark you are died and exited from the game.')

        elif play == 'e':
            print('You are exited from the game.')

    else:
        print('You have entered the wrong input! you are died and exited from the game.')


def r_direction(play):
    
    if play == 'r':
        print('Their is a boat near the river do you want to take and cross the river or do you want go inside the river.')
        play = input('To go inside the river (Press "i") / To pickup the boat (Press "b") : ')

        if play == 'i':
            print('You are Entered into the river.')
            play = input('You will find a shipwrecks do you want to go inside. \n To go inside (Press "g") / To exit (Press "e") : ').lower()

            if play == 'g':
                print('wow! you find a box.')
                play = input('Do you want to open it.To open (Press "o") / If not (Press "n") : ').lower()

                if play == 'o':
                    print('Oops! You are died and exited from the game.')
                elif play == 'n':
                    print('You are eaten by the shark! You are died and exited from the game.')
            else:
                print('You are exited from the game.')

        elif play == 'b':
            play = input('You are in the boat now do you want to cross the river and go into the forest. (y/n) : ').lower()

            if play == 'y':
                print('You have reached the forest.\n Now their is a house in the middle of the forest and 2 gold coins near the house')
                play = input('Do you want to enter into the house. If Yes (Press "d") / (Press "c") : ').lower()

                if play == 'd':
                    print('Hoo No! You are killed by the ghost you are died and exited from the game.')

                else:
                    print('You are exited from the game.')

            else:
                print('You are exited from the game.')


        else:
            print('You have entered the wrong input! you are died and exited from the game.')
    

def u_direction(play):

    if play == 'u':
        print('Do you want to climb the mountain.\n To climb the mountain (Press "m") / To exit (Press "e") : ')

        if play == 'm':
            print('Uf! you have climbed the mountain successfully.')
            play = input('See thier is a box with the name Treasure. \n Do you want to open (Press "o") / you want to jump from the mountain (Press "j") : ').lower()

            if play == 'o':
                print('Haha! You got fooled! Box is empty.')
                a = input('Press "b" : ')

                if a == 'b':
                    print('Naaah!! you are jumped from the mountain')
                    print('you are died and exited from the game.')

            elif play == 'j':
                print('You are died and exited from the game.')

        elif play == 'e':
            print('You are exited from the game.')
        
    else:
        print('You have entered the wrong input! you are died and exited from the game.')



def d_direction(play):

    if play == 'd':
        play = input('Do you want to enter into the black hole (Press "b") / You want to Quit! (Press "q") : ').lower()

        if play == 'b':
            print('Their is a dark inside the hole.')
            play = input('Do not try to turn on the light? Their is a Ghost. \n Still you want to turn on the lights (Press "l") / you want to Quit (Press "q") : ').lower()

            if play == 'l':
                print("Oh! no you find a box. Please don't open it.")
                a = input('May be there is a bomb inside the box. Do you want to open it (Press "d") / Quit (Press "e") : ')

                if play == 'd':
                    print('Congrats!------ {User} You found a Treasure You won the game ------')

                else:
                    print('Boom! You are died and exited from the game')
            
            else :
                print('You are exited from the game.')

        elif play == 'q':
            print('You are exited from the game.')
        
    else:
        print('You have entered the wrong input! you are died and exited from the game.')

def Exit():
    
    User = input('Do you want to exit from the game? (y/n) : ').lower()
    if User == 'y':
        print('You are exited from the game.')
    elif User == 'n':
        you = input('Do you want to start the game again! (y/n) : ').lower()
        if you == 'y':
            startGame()
        else:
            print('You are exited from the game.')

    else:
        print('You have entered the wrong input.')
        Exit()



User = input("Hey What's up? Enter your name : ")
game(user(User))
