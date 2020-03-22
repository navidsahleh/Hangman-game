import random

def randomchoose():
    L=[]
    with open('sowpos.txt','r') as f:
        line=f.readline().strip()
        while line:
            L.append(line)
            line=f.readline().strip()
    k=random.randint(0,len(L))
    z=L[k]
    z=str(z)
    return z

def Hangman():
    print("welcome to Hangman!")
    A=randomchoose()
    set_word=set()
    K=list(A)
    guessnum=6
    L="_" * len(K)
    L=list(L)
    while "".join(L)!=A:
        if guessnum==0:
            print("the word was :","***",A,"***")
            print("sorry! you lose! :(")
            j=input("want to play again? (yes or no) ")
            if j=="yes" :
                p=Hangman()
                return p
            else :
                return "gameover"
        print("(you only have",str(guessnum),"guesses!)")
        guess=input("Guess your letter: ")
        if guess=='stop' :
            return "game over! "
        guess=guess.upper()
#        while guess in L:
#            print("you already said this word!")
#            guess=input("guess again: ")
#            guess=guess.upper()
        z=False
        T=True
        while T:
            if guess in set_word:
                print("you already said this word!")
                guess=input("guess again: ")
                if guess=="stop" :
                    return "game over"
                guess=guess.upper()
            else:
                set_word.add(guess)
                T=False
            
        for i in range(0,len(K)):
            if guess==K[i]:
                L[i]=guess
                z=True
        if z==False:
            guessnum-=1
            print("incorrect!")
        else:
            print(" ".join(L))
    print("you guess correct! :D")
    j=input("want to play again? ")
    if j=="yes" :
        p=Hangman()
        return p
    else:
        return "gameover"

print(Hangman())