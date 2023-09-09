from stages import slownik
import os
from win import win_word
import random
from hasla import uniquewords

word = random.choice(uniquewords)

def wisielec(word):
    word = str(word)
    word = word.lower()
    actually_stage = ""
    wrong = 0
    stage = "stage"
    rletters = list(word)               # tablica z pojedyńczymi literkami, przykładowo ['k', 'o', 't']
    board = ["__"] * len(word)          # tablica z pustymi polami, przykładowo ['__', '__', '__']
    win = False
    print("Gra w wisielca")

    while wrong < 10:
        print("\n")
        msg = "Odgadnij literę: "       # msg = wiadomość "Odgadnij literę"
        char = input(msg)               # char = pojedyncza litera
        char = char.lower()
        if char == word:
            correct = char.split()
            board = correct
        elif char in rletters:
            cind = rletters.index(char) # indeks wystąpienia podanej litery
            board[cind] = char          # zastąpienie pustego pola literką
            rletters[cind] = '$'        # zamiana odgadniętej litery na $
        else:
            wrong += 1
            for i in range(1):
                stage = stage + str(wrong)
                stage_level = stage
                actually_stage = "\n".join(slownik(stage_level))
                stage = "stage"
        print(" ".join(board))
        print(actually_stage)
        if "__" not in board:
            os.system('cls' if os.name == 'nt' else 'clear') 
            print("\nWygrałeś!")
            print(win_word)
            print("\nHasło to było:", "".join(board))
            win = True
            break

        
wisielec(word)