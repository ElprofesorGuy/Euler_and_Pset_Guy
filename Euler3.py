import math
print("Welcome to the Project Euler N°3 : Largest Prime Factor")

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

if __name__=="__main__":
    square_root = int(math.sqrt(600851475143))
    list_of_prime_number = crible_erastosthène(square_root)
    for i in range(len(list_of_prime_number)-1, 0, -1):
        if 600851475143%list_of_prime_number[i]==0:
            print("The largest prime factor of 600851475143 is :", list_of_prime_number[i])
            break
        else:
            continue