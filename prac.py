import random

def guessthenum():
    print('Welcome to the game of guesses\nYou have to enter a no. between 1 and 7')
    print('Good Luck\n')
    ch = 'Y'
    while ch == 'y' or ch == 'Y' :
        num = int(input('Enter you guess: '))
        a = random.randint(1,7)
        if a == num:
            print('Wow, what a luck u have !!! correct\n')
        elif a> num or a< num:
            print('Close enough!!!\n')
        print('The no. selected was',a,'\n')
        ch = input('Do you want to play again?  (Y/N) : \n')
    print('Thank you for playing!!! ')
    quit()
guessthenum()
