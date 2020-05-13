import funcs
import random

print('\t\t.....My Programs.....')
print(' \t\t~ By Haresh Nayak')
player_name = input('\n Please enter your name : ')
print('\n\tGreetings, ' + player_name + '! Welcome to My Programs\n')
op=1
while op != 0 :
    print('press 1 for calculator \npress 2 for game Stone Paper Scissors \npress 0 for exiting')
    op = int(input('Enter your Choice : '))
    if funcs.validate(op):
        if op == 2 :
            print('\n\n\tWelcome to the game of Stone, Paper and Scissors')
            print('Pick a hand : \n 0 for Stone \n 1 for Paper \n 2 for Scissors')
            ch = 'y'
            while ch == 'y' or ch == 'Y' :
                player_hand = int(input('\nPlease enter the number(0-2) : '))
                if funcs.validate(player_hand):
                    computer_hand = random.randint(0,2)
                    funcs.display(player_hand, player_name)
                    funcs.display(computer_hand, 'Computer')
                    result = funcs.judge(player_hand,computer_hand)
                    print('Result : ' + result)
                else:
                    print('\n Enter a valid number(0-2) : ')
                ch  = input('play again?? (Y/N) : ')
            print('\n\t.....Thank you for playing......')

        elif op==1 :
            print('\n\n\t.....Welome to the calculator.....\n')
            print('Enter the two numbers : A and B\n')
            A = int(input('A : '))
            B = int(input('B : '))
            oop =1
            print('Press 1 for adding A+B \nPress 2 for subtrating A-B \nPress 3 for subtracting B-A')
            print('Press 4 for multipying A x B \nPress 5 for dividing A/B \nPress 6 for dividing B/A')
            while oop !=0 :
                oop = int(input('Enter Choice : '))
                if funcs.validate2(oop):
                    if oop  == 1 :
                        print('\nA + B = ' + str(funcs.add(A,B)))
                    elif oop  == 2 :
                        print('\nA - B = ' + str(funcs.sub(A,B)))
                    elif oop  == 3 :
                        print('\nB - A = ' + str(funcs.sub(B,A)))
                    elif oop  == 4 :
                        print('\nA x B = ' + str(funcs.prod(A,B)))
                    elif oop  == 5 :
                        print('\nA / B = ' + str(funcs.divide(A,B)))
                    elif oop  == 6 :
                        print('\nB / A = ' + str(funcs.divide(B,A)))
                else:
                    print('\n Enter a valid number(0-6) : \n')
                    
            print('\t\t......Exiting Calculator.....')
        else :
            print('\t\t.....Thanks for you time......')
            print('\t\t.....Bye!! Have a nice day!......')
    else:
        print('\n Enter a valid number(0-2) : ')
