import math
import random
import string

VOWELS = 'aeiou'
CONSONANTS = 'bcdfghjklmnpqrstvwxyz'
HAND_SIZE = 7

SCRABBLE_LETTER_VALUES = {
    'a': 1, 'b': 3, 'c': 3, 'd': 2, 'e': 1, 'f': 4, 'g': 2, 'h': 4, 'i': 1, 'j': 8, 'k': 5, 'l': 1, 'm': 3, 'n': 1, 'o': 1, 'p': 3, 'q': 10, 'r': 1, 's': 1, 't': 1, 'u': 1, 'v': 4, 'w': 4, 'x': 8, 'y': 4, 'z': 10, '*':0
}

WORDLIST_FILENAME = "words1.txt"

def load_words():
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # wordlist: list of strings
    wordlist = []
    for line in inFile:
        wordlist.append(line.strip().lower())
    print("  ", len(wordlist), "words loaded.")
    return wordlist

def get_frequency_dict(sequence):
    # freqs: dictionary (element_type -> int)
    freq = {}
    for x in sequence:
        freq[x] = freq.get(x,0) + 1
    return freq
	
# Problem #1: Scoring a word
def get_word_score(word, n):
    score=0
    word=word.lower()
    wordlen=len(word)
    for char in word:
        score+=SCRABBLE_LETTER_VALUES[char]
    score= score * abs(((7*wordlen) - 3*(n-wordlen)))
    if score>1 and wordlen!=0:
        return score
    elif score<1 and wordlen!=0:
        return 1
    else:
        return 0
""" n : int >=0
    word : string
    return score(int)"""
    
def display_hand(hand):
    for letter in hand.keys():
        for j in range(hand[letter]):
             print(letter, end=' ')      # print all on the same line
    print()   
    """ hand={'a':1, 'e':2, 'r':1, 's':1, 'n':1, 'd':1}
    display_hand(hand): a e e r s n d """


def deal_hand(n):
# cette fonction tire au hasard trois voyelles et 4 consonnes pour constituer un jeu de lettres.
# Notez que dans ce jeu de lettres, une des voyelles sera remplacé par une lettre joker
# Donc finalement, on a 2 voyelles, un joker et 4 consonnes. Une lettre peut avoir plusieurs occurences
#dans le jeu
    hand={}
    num_vowels = int(math.ceil(n / 3))

    for i in range(num_vowels):
        x = random.choice(VOWELS)
        hand[x] = hand.get(x, 0) + 1
    str=[]
    for elt in hand:
        if elt in VOWELS:
            str.append(elt)
    str=''.join(str)
    y=random.choice(str)
    hand[y]-=1
    if hand[y]!=0:
        hand['*']=1
    else:
        del hand[y]
        hand['*']=1
        
    for i in range(num_vowels, n):    
        x = random.choice(CONSONANTS)
        hand[x] = hand.get(x, 0) + 1
    
    return hand
"""n: int >= 0
    returns: dictionary (string -> int)
    """
#
# Problem #2: Update a hand by removing letters
# Cette fonction met à jour la main de lettres dont dispose le joueur en enlevant les lettres utilisées
#par le joueur pour former le mot. Il faut noter que cette fonction ne modifie pas la chaine initiale
# elle renvoie un dictionnaire qui contient les lettres que le joueur n'a pas utilisé
def update_hand(hand, word):
    hand2=hand.copy()
    for letter in word:
        if letter in hand2.keys() and hand2[letter] > 0:
            hand2[letter]-=1
            if hand2[letter]==0:
                del hand2[letter]
    return hand2
    """word: string
    hand: dictionary (string -> int)    
    returns: dictionary (string -> int)
    """

# Problem #3: Test word validity
# Cette fonction vérifie si le mot entré par le joueur correspond à un des mots du dictionnaire. De plus
# le joueur ne peut utiliser que les lettres qu'il possède dans son jeu de lettres. Donc s'il utilise
#des lettres qu'il n'a pas, le mot formé est considéré comme invalide
def is_valid_word(word, hand, word_list):
    Hand=update_hand(hand.copy(), word)
    word=word.upper()
    is_in_word_list=False
    test_hand=False
    for elt in word_list:
        if match_with_gaps(word, elt):
            is_in_word_list=True
            break
    if len(word)==sum(hand.values()) - sum(Hand.values()):
        test_hand=True
    return is_in_word_list and test_hand
"""word: string
    hand: dictionary (string -> int)
    word_list: list of strings
    returns: boolean
    """

# Cette fonction se charge de comparer le mot entré par le joueur correspond à un mot de la word_list
# Dans l'éventualité ou le joueur utilise un joker, cette fonction vérifie s'il existe des mots de la word_list
#qui peuvent matcher avec le mot proposé en remplaçant le joker par une lettre.
def match_with_gaps(my_word, other_word):
    counter=0
    my_word_copy=my_word[:]
    other_word=list(other_word.upper())
    my_word = list(my_word.upper())
    for i in range(len(my_word)):
        if len(my_word)==len(other_word):
            if my_word_copy[i].isalpha() and my_word_copy[i]==other_word[i]:
                counter+=1
    for char in my_word_copy:
        if char=='*':
            my_word.remove(char)
    return counter == len(my_word)
""" my_word : string
other_word: string
return boolean
"""
#
# Problem #5: Playing a hand
#
def calculate_handlen(hand):
    """hand: dictionary (string-> int)
    returns: integer
    """
    return sum(hand.values())

def play_hand(initial_hand, word_list):
    """score=0
    while sum(hand.values) > 0: # a hand finished when the user input !! or when there is no more letter unused
        print("Current hand : ", display_hand(hand))# the hand is displayed
        word=input("Enter word or !! to indicate that you are finished : ") # ask the user to input a word
        if word == "!!": # if the user input "!!", that means he want to end the game
            print("Total score : ", score)
            break
        else: # if the user input a word different of !!
            if is_valid_word(word, hand, word_list): #we check if that word is valid
                score+=get_word_score(word) # if is a valid word, we print the score of the word
                print(word, " earned ", get_word_score(word), ". Total : ", score)
                hand=update_hand(hand, word) #the remaining letter are displayed 
            while  not is_valid_word(word): # while the user enter an invalid word, a message is displayed
# asking the user to input another word until he input a valid word
                print("You have entered an invalid word!!! Enter another word.\n")
                word=input("Enter word or !! to indicate that you are finished : ")
                score+=get_word_score(word)
                print(word, " earned ", get_word_score(word), ". Total : ", score)
                hand=update_hand(hand, word)
    return score"""
    score=0
    hand=initial_hand.copy()
    while sum(hand.values()) > 0:
        print("Current hand :", end=' ')
        display_hand(hand)
        word=input("\nEnter word or !! to indicate that you are finished : ")
        while  not is_valid_word(word, hand, word_list) and word != '!!':
                    print("\nYou have entered an invalid word!!! Enter another word.\n")
                    word=input("\nEnter word or !! to indicate that you are finished : ")
        if word == '!!':
                print("\nTotal score : ", score)
                break
        else:
            if is_valid_word(word, hand, word_list):
                score+=get_word_score(word, len(hand))
                print("\n\n", word, " earned ", get_word_score(word, len(hand)), ". Total : ", score)
            hand=update_hand(hand, word)
    print("\n\nEnd of the hang game. Your total score  for this hand is : ", score)
    print("\n_____________________\n")
        #replay_hand=input("Would you like to replay this hand ? ")
        #while replay_hand != "yes" or replay_hand != "no":
        #    print("Please enter yes or no.\n")
        #   replay_hand=input("Would you like to replay this hand ? ")
        #if replay_hand == "no":
        #    number_hand-=1
        #    initial_hand = deal_hand(HAND_SIZE)
    return score
"""hand: dictionary (string -> int)
      word_list: list of lowercase strings
      returns: the total score for the hand"""

# Problem #6: Playing a game
# procedure you will use to substitute a letter in a hand
#

def substitute_hand(hand, letter):
    """ 
    Allow the user to replace all copies of one letter in the hand (chosen by user)
    with a new letter chosen from the VOWELS and CONSONANTS at random. The new letter
    should be different from user's choice, and should not be any of the letters
    already in the hand.

    If user provide a letter not in the hand, the hand should be the same.

    Has no side effects: does not mutate hand.

    For example:
        substitute_hand({'h':1, 'e':1, 'l':2, 'o':1}, 'l')
    might return:
        {'h':1, 'e':1, 'o':1, 'x':2} -> if the new letter is 'x'
    The new letter should not be 'h', 'e', 'l', or 'o' since those letters were
    already in the hand."""

    if letter not in hand:
        return hand
    else:
        hand_copy=hand.copy()
        LETTERS= VOWELS+CONSONANTS
        LETTERS= ''.join([elt for elt in LETTERS if elt not in hand])
        y=random.choice(LETTERS)
        hand_copy[y]=hand[letter]
        del hand_copy[letter]
        return hand_copy
    
    """hand: dictionary (string -> int)
    letter: string
    returns: dictionary (string -> int)
    """
    
    
       
    
def play_game(word_list):
    """
    Allow the user to play a series of hands

    * Asks the user to input a total number of hands

    * Accumulates the score for each hand into a total score for the 
      entire series
 
    * For each hand, before playing, ask the user if they want to substitute
      one letter for another. If the user inputs 'yes', prompt them for their
      desired letter. This can only be done once during the game. Once the
      substitue option is used, the user should not be asked if they want to
      substitute letters in the future.

    * For each hand, ask the user if they would like to replay the hand.
      If the user inputs 'yes', they will replay the hand and keep 
      the better of the two scores for that hand.  This can only be done once 
      during the game. Once the replay option is used, the user should not
      be asked if they want to replay future hands. Replaying the hand does
      not count as one of the total number of hands the user initially
      wanted to play.

            * Note: if you replay a hand, you do not get the option to substitute
                    a letter - you must play whatever hand you just had.
      
    * Returns the total score for the series of hands

    

    word_list: list of lowercase strings
"""
    score=[]
    total_score=0
    number_of_hands=int(input("Enter total number of hands : ")) # ask the user to input the total number of hands he wants to play
    while number_of_hands>0: # while the number of hands is positive, the game is still continue
        score=[]
        print("number of hands : ", number_of_hands)
        initial_hand=deal_hand(HAND_SIZE) # loading of the hand
        print("Current hand :", end=' ') # display hand
        display_hand(initial_hand)
        answer = input("Would you like to substituate a letter ? ") # ask the user if he want to substituate one letter in the hand
        while answer != "yes" and answer != "no": # the user must enter only yes or no
            print("\nPlease enter yes or no.\n")
            answer = input("Would you like to substituate a letter ? ")
        if answer == "yes": # if he want to substituate a letter
            replace_letter=input("Which letter do you want to substituate ? ") # ask the user to input the letter he want to substituate
            hand=substitute_hand(initial_hand, replace_letter) # we substituate the letter
            score.append(play_hand(hand, word_list)) # the hand is play until there is no more letter unused or the user input !! 
            hand_play_counter=1
            replay_hand=input("Would you like to replay this hand ? ") # ask the user if he want to replay this hand in order to have a bigger score
            while replay_hand != "yes" and replay_hand != "no":
                print("Please enter yes or no.\n")
                replay_hand=input("Would you like to replay this hand ? ")
            """if replay_hand == "no": # if the answer is no, the user start playing another hand
                number_of_hands-=1
                total_score=score[0]
                initial_hand = deal_hand(HAND_SIZE)
                total_score+=play_hand(initial_hand, word_list)"""
            if replay_hand == "yes":
                score.append(play_hand(hand, word_list))
                total_score += max(score)
                number_of_hands-=1
            else:
                total_score+=int(score[0])
                print("total score ", total_score)
                number_of_hands-=1

        else: # none letter of the hand is not substituate
            score.append(play_hand(initial_hand, word_list))
            replay_hand=input("Would you like to replay this hand ? ")
            while replay_hand != "yes" and replay_hand != "no":
                print("Please enter yes or no.\n")
                replay_hand=input("Would you like to replay this hand ? ")
            """if replay_hand == "no":
                number_of_hand-=1
                initial_hand = deal_hand(HAND_SIZE)"""
            if replay_hand == "yes":
                score.append(play_hand(initial_hand, word_list))
                total_score += max(score)
                number_of_hands-=1
            else:
                total_score+=int(score[0])
                print("total score ", total_score)
                number_of_hands-=1
    
    print("Total score for this game : ", total_score)

if __name__ == '__main__':
    word_list = load_words()
    play_game(word_list)