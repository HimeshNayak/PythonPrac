#exercises from Practice Python
import funcs
#ex.1
def enter():
    o = 'y'
    while o == 'y' or o== 'Y' :
        n=input("Name : ")
        a=int(input('age : '))
        print('Your name is ',n,'\n Your age is ',a)
        c = 100 - a
        year = 2019 + c
        print('You will beacome a 100 year old in the year ',year)
        o = input('Another ? (Y/N) : ')

#ex.2

def oddeven():
    o='y'
    while o == 'y' or o== 'Y' :            
        n=input('Enter your number : ')
        n=int(n)
        if n/2 ==0 :
            print(n,' is an even number')
        elif n/2 != 0:
            print(n,' is an odd number')
        o = input('Check for another number ? (Y/N) : ')


#ex.3

def printbig30():
    a = [79,35,1,778,22,34,17,29,90]      
    for i in a:
        if i>30:
            print (i)  
        

#ex.5
def enterlists():
        a = []
        b = []
        i = 1
        print('Enter the no. of values you want to enter in list a : ')
        numa = int(input())
        print('entering value for a : ')
        cka = 0
        while cka < numa:
            print('[',i,']')
            aa = int(input())
            a.append(aa)
            i+=1
            cka += 1

        j = 1
        print('\n\n Enter the no. of values you want to enter in list b : ')
        ckb = 0
        numb = int(input())
        print ('\n Entering values for b :')
        while ckb < numb: 
            print('[',j,']')
            bb = int(input())
            a.append(bb)
            j+=1
            ckb +=1    
        d = []
        for i in a :
            for j in b :
                if i == j :
                    print(i)

#ex.4


def factors():
    i = 1
    n = int(input('enter the no. of which you want to find the factors : '))
    print('The factors of the given no. ', n ,' are : ')
    while i<=n : 
        if n%i == 0 :
            print(i)
        i+=1



#ex.6
def palin():
    n = str(input('Enter a string to check whether it is a palindrome or not : '))
    i = 0
    j = len(n)-1
    while i!= j : 
        if n[i] == n [j] : 
            print('palindrome string')
            continue
        elif n[i]!= n[j] :
            print('Not a palindrome string...')
            break 
        i+=1
        j-=1


a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
funcs(a,b)


















                    


