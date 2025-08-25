#cette fonction détermine si une chaine de carectères est un palindrome
def ispalindrome(string):
    return string == string[::-1]

def convertion_binaire(num): #cette fonction convertit un nombre de la base 10 vers la base 2
    remainder_list=[]
    r=0
    while num>0:
        r=num%2
        remainder_list+=str(r)
        num=int(num/2)
    lenght=len(remainder_list)
    binary_code=[]
    for i in range(0, lenght):
        binary_code+=str(remainder_list[lenght-i-1])
    return binary_code

#Cette fonction permet de supprimer les 0 non significatifs ie les 0 situés avant la 1ère occurence
# du chiffre 1 dans le code binaire
def remove_unsignificant_number(binary_number): 
    i=0
    while binary_number[i]==0:
        del(binary_number[i])
        i+=1
    return binary_number

print("Welcome to the project Euler N°36: Double-Base Palindromes")
sum_of_palindrome=0
for i in range(1,1000001):
    if ispalindrome(str(i)):
        if ispalindrome(convertion_binaire(i)):
            print(i)
            sum_of_palindrome+=i
print("The sum of all the number less than 1000000 which are palindrom in base 10 and 2 is " +str(sum_of_palindrome))


