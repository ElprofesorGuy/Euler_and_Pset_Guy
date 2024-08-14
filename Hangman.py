import string
import random


WORDLIST_FILENAME = "words.txt"


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

#Fonction principale du jeu
if __name__ == '__main__':
    new_game=1
    while new_game==1:
        number_of_helping=1
        number_of_warning=3
        numbers_of_guess=6
        secret_word = choose_word(wordlist)
        guess_word=["_"]*len(secret_word)
        guess_word=''.join(guess_word)
        available_letters=string.ascii_lowercase
        print("Welcome to the game Hangman\n")
        print("I am thinking of a word that is "+str(len(secret_word))+ " letters long\n_ _ _ _ _ _ _")
        while guess_word!=secret_word and numbers_of_guess>0:
            print("\nYou have"+str(number_of_warning)+" warning left")
            print("\nYou have "+str(numbers_of_guess)+" guessed left.\n")
            print("Available letters : ", end='')
            for char in available_letters:
                print(char, end=' ')
            letter_guessed=(input("\n\nPlease guess a letter: ")).lower()
            #cette fonction permet de bloquer l'entrée des caractères spéciaux par l'utilisateur. Tant qu'il n'entre pas
            # pas une lettre présente en available_letters, un message d'erreur lui ai renvoyé. Le joueur ne peut non plus 
            #demander de l'aide d'entrée de jeu.
            while (letter_guessed.isalpha() == False): 
                if letter_guessed=='*' and number_of_helping>0:
                    number_of_helping-=1
                    print("Possible word matches are: ")
                    show_possible_matches(guess_word)
                    print("\n")
                else:
                    if number_of_warning==0:
                        numbers_of_guess-=1
                        print("\nOops ! That is not a valid letter. You have "+str(numbers_of_guess)+" guess left. ",end='')
                        print_with_space(guess_word)
                        print("\n")
                    else:
                        number_of_warning-=1
                        print("\nOops ! That is not a valid letter. You have "+str(number_of_warning)+" warning left. ",end='')
                        print_with_space(guess_word)
                        print("\n")
                letter_guessed=(input("Please guess a letter: ")).lower()
        #cette fonction se charge d'emmpêcher la validation d'une réponse contenant plusieurs lettres   
            while len(letter_guessed)!=1:
                if len(letter_guessed)<1:
                    print("You have not entered a letter!!!")
                    letter_guessed=(input("Please guess a letter: ")).lower()
                else:
                    print("Oops, you should enter only 1 letter, not more!!!")
                    letter_guessed=(input("Please guess a letter: ")).lower()
        #cette boucle affiche un message à l'utilisateur si ce dernier entre une lettre qu'il avait déjà entré
        #plus tôt
            while check_letter(available_letters,letter_guessed):
                if number_of_warning==0:         
                    numbers_of_guess-=1
                    print("\nOops ! You have already guessed this letter. You have "+str(numbers_of_guess)+" guess left. ",end='')
                    print_with_space(guess_word)
                    print("\n")
                else:
                    number_of_warning-=1
                    print("\nOops ! You have already guessed this letter. You have "+str(number_of_warning)+" warning left. "+guess_word)
                letter_guessed=(input("Please guess a letter: ")).lower()
            available_letters=get_available_letters(available_letters,letter_guessed)
            if get_guessed_word(secret_word,letter_guessed,guess_word)!=guess_word:
                print("Good guess: ", end=' ')
                print_with_space(get_guessed_word(secret_word, letter_guessed,guess_word))
                print("\n____________")
            else:
                print("\nOops! That letter is not in a word: ", end=' ')
                print_with_space(get_guessed_word(secret_word, letter_guessed,guess_word))
                numbers_of_guess-=1
                print("\n\n____________\n\n")
            guess_word=get_guessed_word(secret_word,letter_guessed,guess_word)
        if guess_word == secret_word:
            print("\nCongratulations, you won the Game.\n")
            print("\nYour total score for this game is: "+str(numbers_of_guess*count_unique_letters(secret_word)))
        else:
            print("\n The correct word is: " + str(secret_word))
        print("Do you want to play a new game???")
        print("1. New game")
        print("2. Exit")
        new_game=int(input())
        while new_game != 1 and new_game != 2:
            print("1. New game")
            print("2. Exit")
            new_game=int(input())