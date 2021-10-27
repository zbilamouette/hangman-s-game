word=['a','c','c','u','m','u','l','e','r']

def hangman(word):
    list=[]
    for k in range(len(mot)):
        list.append('_')
    show(list)
    while True:
        guess = str(input('Guess :'))
        if guess==''.join(mot):
            win()
        for k in range(len(mot)):
            if mot[k-1]==guess:
                list[k-1]=guess
        show(list)
        check_win(list)


def show(list):
    print(' '.join(list),'\n')


def check_win(list):
    c=0
    for a in range(len(list)):
        if list[a]!='_':
            c+=1
    if c==len(list):
        win()


def win():
    print('You win Bro !')



if __name__ == "__main__":
    hangman(word)
