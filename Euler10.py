print("Welcome to the project Euler N°10 : Summation of prime")
tab=[]
for i in range(2000000):
    tab.append(True)
tab[0]=False
tab[1]=False

for p in range(2,2000000):
    if tab[p] != False:
        k=2
        while k*p <= 1999999:
            tab[k*p]=False
            k+=1
sum_of_prime=0
for p in range(2,2000000):
    if tab[p]==True:
        sum_of_prime+=p
print(sum_of_prime)