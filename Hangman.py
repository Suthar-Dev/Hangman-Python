import random
while True:
    print('Welcome To HANGMAN')
    print()
    print()
    print('      O       ')
    print('     /|\      ')
    print('      |       ')
    print('     / \      ')
    print()
    print()
    print(' The person giving the word should be in control now')
    print()
    W = input('Enter your word here: ')
    w = W.lower()
    Word = []
    for k in range(20):
        print('|')
    print('V')
    for k in w:
        Word.append(k)
    L = len(Word)
    if L >2 and L<=4:
        r = random.randint(0,L-1)
        k = 0
        l = []
        while k<L:
            if k == r:
                l.append(Word[r])
            else:
                l.append('_')
            k += 1
    if L>4 and L<=7:
        r = random.randint(0,L//2)
        R = random.randint(L//2+1,L-1)
        k = 0
        l = []
        while k<L:    
            if k == r:
                l.append(Word[r])
            elif k == R:
                l.append(Word[R])
            else:
                l.append('_')
            k += 1
    if L>7 and L<15:
        r = random.randint(0,L//3)
        R = random.randint(L//3+1,2*L//3)
        rR = random.randint(2*L//3+1,L-1)
        k = 0
        l = []
        while k<L:
            if k == r:
                l.append(Word[r])
            elif k == R:
                l.append(Word[R])
            elif k == rR:
                l.append(Word[rR])
            else:
                l.append('_')
            k += 1
    print()
    for k in l:
        print(k,end = ' ')
    print()
    print()
    print('Person Guessing the word must now be in control')
    print('This is your word ^')
    print()
    D = 0
    m = 0
    J = l
    while D <= L or m <= 5:
        G = input('Guess a letter: ')
        print()
        n = 0
        for k in range(L):
            if G != Word[k]:             
                n += 1                   
            elif G == Word[k]:
                J.pop(k)
                J.insert(k,Word[k])
        for k in J:
            print(k,end = ' ')
        print()
        print()
        if J == Word:
            print()
            print('CONGRATULATIONS, YOU WIN')
            print()
            break
        if n == L:
            print()
            print('Oh no, this letter is not in the word')
            print()
            m +=1
        if m == 1:
            print()
            print()                         
            print('      O       ')         
            print('     /|\      ')         
            print('      |       ')
            print('     /       ')
            print()
            print()
        if m == 2:
            print()
            print()
            print('      O       ')
            print('     /|\      ')
            print('      |       ')
            print()
            print()
        if m == 3:
            print()
            print()
            print('      O       ')
            print('     /|      ')
            print('      |       ')
            print()
            print()
        if m == 4:
            print()
            print()
            print('      O       ')
            print('      |      ')
            print('      |       ')
            print()
            print()
        if m == 5:
            print()
            print()
            print('             ')
            print('      |      ')
            print('      |       ')
            print()
            print()
            print('GAME OVER')
            print()
            print('The word was: ',w)
            print()
            break
        D += 1
    print()
    print('Press 0 to end or Press 1 to continue')
    print()
    qwerty = int(input('Enter here: '))
    if qwerty == 0:
        break
    elif qwerty == 1:
        continue
    else:
        print()
        print('Invalid Option')
        print()
        break
print()
print('THANK YOU FOR PLAYING!')
print()
        
    
