import string
import random


WORDLIST_FILENAME = "words.txt"
play_again=1



def load_words():
    print("Loading word list from file...")
    inFile = open(WORDLIST_FILENAME, 'r')
    line = inFile.readline()
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist



def choose_word(wordlist):
    return random.choice(wordlist)

wordlist = load_words()


#A chaque fois que l'utilisateur trouve une lettre du mot secret, cette fonction affiche un mot comportant
# les lettres déjà devinés par le joueur et celles qui n'ont pas encore été devinées.    
def get_guessed_word(secret_word, letters_guessed, guess_word):
    guess_word=list(guess_word)
    lower_letters=letters_guessed.lower()
    for index1 in range(0,len(letters_guessed)):
        for index2 in range(0,len(secret_word)):
            if lower_letters[index1]==secret_word[index2]: 
                guess_word[index2]=secret_word[index2]
    return ''.join(guess_word)

def check_letter(word,letter):    #cette fonction verifie si une lettre est dans un mot et dans ce cas
    return letter.lower() in word.split()


#Affichage des lettres pas encore entré par le joueur. Une fois qu'il entre une lettre, cette lettre est
# retiré des possibles. Si le joueur entre une lettre qu'il avait déjà entré, il perd en number_of_guess

def get_available_letters(available_letters,letter_guessed):
    list_letters=list(available_letters)
    lower_letter=letter_guessed.lower()
    for char in list_letters:
        if char == letter_guessed:
            list_letters.remove(char)
    return ''.join(list_letters)
#cette fonction compte le nombre de lettres uniques d'un mot
def count_unique_letters(word):
    counter=len(word)
    for i in range(len(word)-1):
        for j in range(i+1,len(word)):
            if word[i]==word[j]:
                counter-=1
    return counter
#cette fonction verifie si le mot forme par les lettres déjà devinées par l'utilisateur peut correspondre
# à un mot de la bibliothèque de mots
def match_with_gaps(my_word, other_word):
    counter=0
    my_word_copy=my_word[:]
    other_word=list(other_word)
    my_word = list(my_word)
    for i in range(len(my_word)):
        if my_word_copy[i].isalpha() and my_word_copy[i]==other_word[i]:
            counter+=1
    for char in my_word_copy:
        if char=='_':
            my_word.remove(char)
    return counter == len(my_word) #si la longueur du mot
#Cette fonction affiche tous les mots qui matchent avec les lettres déjà trouvé par l'utilisateur    
def show_possible_matches(my_word):
    for string in wordlist:
        if len(string) == len(my_word):
            if match_with_gaps(my_word,string):
                print(string, end=' ')

def print_with_space(word):
    for char in word:
        print(char, end=' ')

#cette foncton renvoir un bool qui servira à savoir si la lettre entrée est valide ou non
def is_it_error(letter, available_letters):
    return letter in string.ascii_letters and letter in available_letters

#cette fonction affiche un message d'erreur en fonction du type d'erreur
def get_error(letter, available_letters):
    if letter not in string.ascii_letters:
        return "\nThat is not a valid letter!!!"
    elif letter not in available_letters:
        return "\nYou have already entered this letter!!!"
    
def hangman(secret_word):
    number_of_helping=1
    number_of_guess=6
    number_of_warning=3
    available_letters=string.ascii_lowercase
    guess_word=''.join(["_"]*len(secret_word))
    print("Welcome to the game Hangman\n")
    print("I am thinking of a word that is "+str(len(secret_word))+ " letters long\n_ _ _ _ _ _ _")
    while guess_word!=secret_word and number_of_guess>0: #le jeu s'arrête quand le mot secret a été trouvé ou quand number_of_guess tombe à 0
            print("\nYou have "+str(number_of_warning)+" warning left")
            print("\nYou have "+str(number_of_guess)+" guessed left.\n")
            print("Available letters : ", end='')
            for char in available_letters:
                print(char, end=' ')
            letter_guessed=(input("\n\nPlease guess a letter: ")).lower()
            while is_it_error(letter_guessed, available_letters)==False: #tant qu'il y' a erreur, la lettre
                # entrée ne sera pas validée
                if letter_guessed=='*' and number_of_helping>0:
                    number_of_helping-=1
                    print("\nPossible word matches are: ")
                    show_possible_matches(guess_word)
                    print("\n_ _ _ _ _ _ _ _ _ _\n")
                    break
                else:
                    print(get_error(letter_guessed, available_letters))#affichage d'un message d'erreur en 
                    # fonction du type d'erreur
                    if number_of_warning>0: #tant que le nbre d'avertissement est non nul, les erreurs sont
                    # déduis de ce nombre
                        number_of_warning-=1
                        if number_of_warning==0:
                            print("\nNO MORE WARNING and "+str(number_of_guess)+" guess left.")
                            print("\n_ _ _ _ _ _ _ _ _ _ \n")
                        else:
                            print("\nYou have "+str(number_of_warning)+" warning left and "+str(number_of_guess)+" guess left!!!\n Your word : ", end=' ')
                            print_with_space(guess_word)
                            print("\n_ _ _ _ _ _ _ _ _ _ \n")
                    elif number_of_warning==0: # une fois le nbre d'avertissement nul, les erreurs sont déduites
                    # du nombre de chances
                        number_of_guess-=1
                        if number_of_guess==0: # une fois que le nombre de chance est nul, le jeu s'arrête
                            print("\nNO MORE GUESS LEFT!!!\n")
                            break
                        else: #affichage du nombre de chances restant
                            print("\nYou have "+str(number_of_guess)+" guess left!!!\nYour word : ", end='')
                            print_with_space(guess_word)
                            print("\n\n_ _ _ _ _ _ _ _ _ _ \n")
                    letter_guessed=(input("\n\nPlease guess a letter: ")).lower()
            available_letters=get_available_letters(available_letters, letter_guessed)#une fois une lettre entrée
                # elle est retirée des lettres valides
            if get_guessed_word(secret_word,letter_guessed,guess_word)!=guess_word: # si la lettre trouvée est bonne
                # on la positionne au bon endroit en tenant compte de ses occurences dans le mot secret
                    print("\n\nGood guess!!! Your word : ", end=' ')
                    print_with_space(get_guessed_word(secret_word, letter_guessed,guess_word))
                    print("\n_ _ _ _ _ _ _ _ _ _ ")
            else:# si c'est pas la bonne lettre, on affiche un message qui le signale
                if letter_guessed!='*':
                    print("\n\nOops! That letter is not in a word. Your word : ", end=' ')
                    print_with_space(get_guessed_word(secret_word, letter_guessed,guess_word))
                    number_of_guess-=1
                    print("\n\n_ _ _ _ _ _ _ _ _ _ \n\n")
            guess_word=get_guessed_word(secret_word,letter_guessed,guess_word)
    if guess_word == secret_word:
            print("\nCongratulations, you won the Game.\n")
            print("\nYour total score for this game is: "+str(number_of_guess*count_unique_letters(secret_word)))
    else:
            print("\n The correct word is: " + str(secret_word))

if __name__ == '__main__':
    while play_again==1:
        secret_word=choose_word(wordlist)
        hangman(secret_word)
        print("Do you want to play a new game???")
        print("1. New game")
        print("2. Exit")
        play_again=int(input())
        while play_again != 1 and play_again != 2:
            print("1. New game")
            print("2. Exit")
            play_again=int(input())