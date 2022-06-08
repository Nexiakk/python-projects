import random
from hangman_data import stages, words

choosen_word = random.choice(words)
blanks = ["_" for x in choosen_word]
entered_letters = set()
zycia = 6

while True:
    print(stages[zycia])
    print(" ".join(x for x in blanks))
    ask_letter = input("Enter a letter: ")
    if len(ask_letter) == 1:
        if ask_letter not in entered_letters:
            if ask_letter in choosen_word.lower() or ask_letter in choosen_word:
                entered_letters.add(ask_letter)
                letter_info = [[k,v] for k,v in enumerate(choosen_word) if v.lower() == ask_letter or v == ask_letter]
                for x in letter_info:
                    blanks[x[0]] = x[1]
                if "_" not in blanks:
                    print(" ".join(x for x in blanks))
                    print("Congrats, you won!")
                    break
            else:
                zycia-=1
                if zycia <= 0:
                    print(stages[zycia])
                    print("Hangman died, you lost!")
                    break
                else:
                    print("Letter is wrong, you lost one life!")
                    entered_letters.add(ask_letter)
        else:
            print("You've already entered this letter.")
    else:
        print("You must enter one letter.")