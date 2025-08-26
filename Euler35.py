
print("Welcome to Project Euler n°35 : Circular primes")

#changeons de disque 
#cette fonction retourne tous les entiers premiers inférieurs à un nombre N
def crible_erastosthène(number):
    list = [True]*(number+1)
    list[0] = list[1] = False
    m = 2
    while (m*m <= number):
        if list[m]:
            for multiple in range(m*m, number+1, m):
                list[multiple]= False
        m+=1
    return [i for i, value in enumerate(list) if value]

#cette fonction détermine les rotations circulaires d'un nombre et retourne une liste
def write_circular_number(number):
    counter=0
    number=list(str(number))
    circular_number_list=['0']*len(number)
    while counter<len(number):
        number_copy=number[:]
        for n in range(0, len(number)):
            if n==len(number)-1:
                number[n]=number_copy[0]
            else:
                number[n]=number_copy[n+1]
        circular_number_list[counter]=''.join(number)
        counter+=1
    return circular_number_list

#cette fonction prend en entrée une liste d'entiers et détermine si tous ses éléments sont premiers
def is_all_prime_number(list_number, list_of_prime_number):
    bool = True
    for elt in list_number:
        if int(elt) not in list_of_prime_number:
            return False
    return bool

#cette fonction détermine si tous les rotations d'un nombre sont des entiers premiers
def is_all_circular_prime(list_of_prime_number):
    counter =0;
    for prime in list_of_prime_number:
        circular_partner = write_circular_number(prime)
        if is_all_prime_number(circular_partner, list_of_prime_number):
            counter+=1
    return counter
        
if __name__ == "__main__":
    resultat = is_all_circular_prime(crible_erastosthène(1000000))
    print("Below one million, we have : ",resultat, "circular primes.")
