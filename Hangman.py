from os import system, name
from time import sleep
HANGMAN_ASCII_ART = print("""  _    _                                         
 | |  | |                                        
 | |__| | __ _ _ __   __ _ _ __ ___   __ _ _ __  
 |  __  |/ _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
 | |  | | (_| | | | | (_| | | | | | | (_| | | | |
 |_|  |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                      __/ |                      
                     |___/""")
again = ""
print('you have 6 tries, good luck!')

def clear():
    #הפונקציה מנקה את המסך
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')

def Print_Hangman(num):
    #הפונקציה מדפיסה את מצבו של האיש התלוי בהתאם לערך שהיא מקבלת
    #:parm num: key of dict\num of faild trys
    #:type num: int
   HANGMAN_LOOK = {1:"""    x-------x 
   
   
   
   
   
   """, 2: """    x-------x
    |
    |
    |
    |
    |""", 3: """    x-------x
    |       |
    |       0
    |
    |
    |""", 4: """    x-------x
    |       |
    |       0
    |       |
    |
    |""", 5: r"""    x-------x
    |       |
    |       0
    |      /|\
    |
    |""", 6: r"""    x-------x
    |       |
    |       0
    |      /|\
    |      /
    |""", 7: r"""    x-------x
    |       |
    |       0
    |      /|\
    |      / \
    |"""}
   print(HANGMAN_LOOK[num])

def check_valid_input(letter_guessed, old_letters):
    #הפונקציה בודקת אם המשתנה המתקבל מהמשתמש תקין לפי מה שהוגדר בתרגיל
    #:param old_letters: all the letters that been gust by the user so far
    #:param letter_guessed: the last letter that been gust by the user
    #:type old_letters: list
    #:type letter_guessed: str
    if len(letter_guessed) > 1 or letter_guessed.isalpha() == False or letter_guessed in old_letters:
        return False
    else:
        return True

def try_update_letter_guessed(letter_guessed, old_letters):
    #במידה והקלט תקין, מוסיף האות המנוחשת למאגר האותיות שנוחשו עד כה
    #:param old_letters: all the letters that been gust by the user so far
    #:param letter_guessed: the last letter that been gust by the user
    #:type old_letters: list
    #:type letter_guessed: str
    if check_valid_input(letter_guessed, old_letters):
        old_letters.append(letter_guessed.lower())
        return True
    elif letter_guessed in old_letters:
        print("X\nyou already tried this letter")
        print(" ---> ".join(sorted(old_letters)))
    else:
        print("Sorry darling, I can only get a single letter (from the abc) at once,\nlets try again, show we?" + '\n\n')
    return False

def show_hidden_word(secret_word, old_letters):
    #הפונקציה מראה את המילה שהמשתמש צריך לנחש, כאשר התו "_" מחילף כל אות שהמשתמש לא ניחש עד כה
    #:param old_letters: all the letters that been gust by the user so far
    #:param secret_word: the word that the user need to gusse
    #:type old_letters: list
    #:type secret_word: str
    guessed_word = ""
    for n in secret_word:
        if n in old_letters:
            guessed_word +=(" "+ n)
        else:
            guessed_word += " _"
    print(guessed_word)

def check_win(secret_word, old_letters):
    #הפונקציה בודקת אם המשתמש ניחש את כל האותיות במילה, ובמידה וכן מחזירה אמת
    #:param old_letters: all the letters that been gust by the user so far
    #:param secret_word: the word that the user need to gusse
    #:type old_letters: list
    #:type secret_word: str
    for n in secret_word:
        if n not in old_letters:
            return False
    return True

def choose_word(file_path, index):
    #הפונקציה בוחרת מילה מתוך מאגר מילים בהתאם למספר שהיא מקבלת
    #:param file_path: the path of the txt file
    #:param index: number from the user
    #:type file_path: str
    #:type index: int
    path = open(file_path, 'r')
    file = path.read().split()
    counter = 0
    index %= len(file)
    word = file[index - 1]
    for n in range(0, len(file)):
        if file.count(file[n]) > 1:
            file[n] = ""
            counter += 1
    return word, (len(file) - counter)

sleep(3)
clear()
words_path = input('For starting our path, I will need you to give me the path for your text file..')
while again != 'exit':
        num = input("hey pal, throw me a number: ")
        secret_word = choose_word(words_path, int(num))[0]
        num_of_tries = 1
        old_letters = []
        Print_Hangman(num_of_tries)
        show_hidden_word(secret_word, old_letters)
        while num_of_tries < 7:
            guess = input("Give me your best shot: ")
            clear()
            if try_update_letter_guessed(guess, old_letters):
                if guess not in secret_word:
                    num_of_tries += 1
                    print("no luck this time):")
            print("you failed " + str(num_of_tries - 1)  + " times")
            Print_Hangman(num_of_tries)
            show_hidden_word(secret_word, old_letters)
            if check_win(secret_word, old_letters):
                clear()
                print("U ARE THE WINNER!!!")
                num_of_tries = 8
        if num_of_tries == 7:
            clear()
            print("sorry mate, you lost):\nmaybe next time")
        sleep(2)
        again = input("for exit type exit\nfor starting again type anything else: ")
