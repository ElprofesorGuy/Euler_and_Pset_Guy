list_unit=['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight','nine']
list_exception=['ten','eleven','twelve','thirteen','fourteen','fifteen','sixteen','seventeen','eighteen','nineteen',
              'twenty']
list_centaine=['one hundred and','two hundred and','three hundred and','four hundred and','five hundred and',
               'six hundred and','seven hundred and','eight hundred and','nine hundred and']
list_dizaine=['twenty','thirty','forty','fifty','sixty','seventy','eighty','ninety']
"""
Ces dictionnaires contiendront des équivalences entre les nombres et leur équivalent en lettre
par exemple, 1 en unité c'est one, en centaine, c'est one hundred. Ainsi de suite jusqu'à 9
Et puis dans dict_exception, il y'a les nombres de 11 à 19
"""

"""
Fonction qui va permettre de décomposer un nombre en unité, dizaine et centaine
"""
def decompose_number(number):
    decomposition_list=[]
    decomposition_list.append(int(number/100))
    decomposition_list.append(int((number - (decomposition_list[0]*100))/10))
    decomposition_list.append(number%10)
    return decomposition_list



"""Fonction qui prend un nombre(entier naturel) en entrée et qui retourne l'écriture en lettres de ce nombre"""
def print_number_in_letter(number):
    decomposition_list=decompose_number(number)
    if len(str(number))==1:
        return dict_unit[number]
    elif len(str(number))==2:
        if number < 21:
            return dict_exception[int(number)]
        elif number>=21 and number%10!=0:
            return dict_dizaine[decomposition_list[1]] + " " + dict_unit[decomposition_list[2]]
        elif number>=21 and number%10==0:
            return dict_dizaine[decomposition_list[1]]
    elif len(str(number))==3:
        if number%100 == 0:#si le nombre est un multiple de 100
            return dict_unit[number/100] + " hundred"
        elif decomposition_list[1]==0 and number%100 != 0:#si le chiffre des dizaines vaut 0
            return dict_centaine[decomposition_list[0]] + " " + dict_unit[decomposition_list[2]]
        elif 10 <= int(number%100) and int(number%100) <= 20:#si le reste du nombre par 100 est compris entre 10&20
            return dict_centaine[decomposition_list[0]] + " " + dict_exception[number%100]
        elif number%10!=0:#si le nombre n'est pas un mutliple de 10
            return dict_centaine[decomposition_list[0]]+" "+dict_dizaine[decomposition_list[1]]+" "+dict_unit[decomposition_list[2]]
        elif number%10==0:#si le nombre est un multiple de 10
            return dict_centaine[decomposition_list[0]]+" "+dict_dizaine[decomposition_list[1]]
    elif len(str(number))>=4 and len(str(number))<=6:#si le nombre a 4 ou 5 chiffres
        thousand=int(number/1000)
        return thousand
        """return print_number_in_letter(thousand)+" thousand "+print_number_in_letter(int(number - thousand*1000))"""

"""
Fonction qui supprime le caractère espace (' ') dans une chaine de caractère
"""
def remove_space(string):
    list_of_string=list(string)
    for elt in list_of_string:
        if elt == " ":
            list_of_string.remove(elt)
    return ''.join(list_of_string)


if __name__ == '__main__':
    dict_unit={}
    dict_exception={}
    dict_dizaine={}
    dict_centaine={}
    for i in range(0, len(list_unit)):
        dict_unit[i+1]=list_unit[i]
        dict_centaine[i+1]=list_centaine[i]
    for u in range(len(list_exception)-1, 21):
        dict_exception[u]=list_exception[u-10]
    for i in range(0, len(list_dizaine)):
        dict_dizaine[i+2]=list_dizaine[i]

    lenght=0
    list_of_number_in_letter=[]
    for i in range(1,1000):
        list_of_number_in_letter.append(print_number_in_letter(i))
    for i in range(len(list_of_number_in_letter)):
        lenght+=len(remove_space(list_of_number_in_letter[i]))

    print("To write all the numbers from 1 to 1000 ", lenght+len(remove_space("one thousand")), "letters should be used")