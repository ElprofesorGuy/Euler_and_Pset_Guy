def ispalindrome(string):
    return string == string[::-1]

print("Welcome to the projet Euler N°4 : Largest Palindrome number.\n")
max=0
a=0
b=0
for i in range(999,99,-1):
    for j in range(999,99,-1):
        if ispalindrome(str(i*j)) == True and i*j>max:
            max = i*j
            a=i
            b=j
print("Le plus grand palindrome est " + str(b*a)+ "="+str(a)+"*"+str(b))
