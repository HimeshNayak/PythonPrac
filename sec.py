print('''\t hey guys!!! \n Now we will do some fun\n But first login into the program \n''')


def calcultor() :
    print('''
                Welcome to the calculator \n
                Hope everything goes well \n INSTRUCTIONS
                for exponents press e as operator
                for obtaining a whole no. as the quotient press w
                for cancelling the program enter 'x' ''','\n\n' ) 
            c = 'Y'
            while c =='y' or c== 'Y':
                    i=int(input("value 1: "))
                    o=input('operator :  ')
                    j=int(input('value2 : '))
                    if o is '+' :
                            r = int(i+j)
                    elif o is '-' :
                            r = int(i-j)
                    elif o is '*' :
                            r = int(i*j)
                    elif o is '/' :
                            r = float(i/j)
                    elif o is 'e' :
                            r = int(i**j)
                    elif o is 'w' :
                            r = int(i//j)
                    else :
                        print('Enter correct operator')
                        continue
                    print(r,'\n')
                    c = input('another?(Y<N): ')
                    print("\n")

def gcd() :
    print ("\n Finding gcd")
        x = 1 
        while x != 0 : 
        a = int(input('Enter the first no.'))
        b = int(input('Enter the second no.'))
        if (a<b) :
            (a,b) = (b,a)

        if (a%b) == 0 :
            return(b)


def login() :
    c=0
    while c<1:
        n=str(input('Name : '))
        p= str(input('Password : '))
        if n=="haresh" and p =="harry":
            print("Hi Haresh! \n Welcome to the program ")
            c=1
        elif n=='Himesh'and p == 'Himmi':
            print("Hi Himesh! \n Welcome to the program")
            c=1
        else:
            c = 0
            print('Invalid login!!! :( ')

login()
print("Now tell me what would you like to do : ")
o=1
while o!=0 :
    print('''\n
    Enter 1 for opening calculator :
    Enter 2 for obtaining greatest common divisor :
    Enter 0 for exiting : ''')
    o = int(input("Enter your choice : ")) 

    if o == 1 :
        calculator()
        
    elif o == 2 :
        
        
    elif o==0 :
        break

