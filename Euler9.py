from math import sqrt

print("Welcome to the project Euler N°9 : Special pythagorean Triplet")

for a in range(1,500):
    for b in range(a,500):
        c=sqrt((a**2)+(b**2))
        if c-int(c)==0 and a+b+int(c)==1000:
            print("valeur de a b et c ", a, b, int(c))
            print("The Pythagorian product is  "+str(a*b*int(c)))
            break
    


