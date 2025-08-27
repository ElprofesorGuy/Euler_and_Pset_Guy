print("Welcome to the Project Euler N°22: Noms Scores")

WORDLIST_FILENAME = "Euler22/name.txt"
LETTERS_POSITION = {
    'A': 1, 'B': 2, 'C': 3, 'D': 4, 'E': 5, 'F': 6, 'G': 7, 'H': 8, 'I': 9, 'J': 10, 'K': 11, 
    'L': 12, 'M': 13, 'N': 14, 'O': 15, 'P': 16, 'Q': 17, 'R': 18, 'S': 19, 'T': 20, 'U': 21,
    'V': 22, 'W': 23, 'X': 24, 'Y': 25, 'Z': 26
}

def load_words():
    print("Loading word list from file...")
    inFile = open(WORDLIST_FILENAME, 'r')
    line = inFile.readline()
    wordlist = line.split('\"')#Suppression des doubles guillemets dans chaque mot
    chaine = ','.join(wordlist)#suppression des virgules qui séparent les mots
    wordlist = chaine.split(',')
    word_list_name = [word for word in wordlist if len(word)>=2]
    print("  ", len(word_list_name), "words loaded.")
    return sorted(word_list_name)#on retourne une liste classée par ordre alphabétique

def sum_of_letter_position_of_word(word):#fais la somme des positions des lettres d'un mot
    score = 0
    for letter in word:
        score += int(LETTERS_POSITION[letter])
    return score

if __name__ == "__main__":
    wordlist = load_words()#chargement de la liste des mots
    total_score = 0
    for i in range(len(wordlist)):
        total_score += (i+1)*sum_of_letter_position_of_word(wordlist[i])
    print("Le score totatl des noms dans le fichier est égal à: ", total_score)