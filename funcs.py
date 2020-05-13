def validate(hand) :
    if hand <0 or hand >2 :
        return False
    return True
def display(hand,name = 'Guest'):
    hands = ['Stone','Paper','Scissors']
    print(name + ' picks : ' + hands[hand])

def judge(player, computer):
    if player == computer :
        return 'Draw'
    elif player == 0 and computer == 1 :
        return 'Loss'
    elif player == 0 and computer == 2:
        return 'Loss'
    elif player == 2 and computer == 0 :
        return 'Loss'
    else:
        return 'win'
def validate2(choice) :
    if  choice<0 or choice >6 :
        return False
    return True
    return True
def add(a,b):
    sum = a+b
    return sum
def sub(a,b):
    diff = a-b
    return diff
def prod(a,b):
    prod = a*b
    return prod
def divide(a,b):
    quot = a/b
    return quot

def common(a,b):
    i,j
    for i in a:
        for j in b:
            if a[i] != b[j]:
                print (a[i])
                break
            else :
                print('NO common element')
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
common(a,b)


