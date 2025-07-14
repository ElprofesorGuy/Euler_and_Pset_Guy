def iterseq(number):
    counter=1
    while number != 1:
        if number%2==0:
            number=number/2
        else:
            number = (3*number)+1
        counter+=1
    return counter

print("Welcome to the project Euler N°14: Longest Collatz Sequence\n")
max=507
value=1000000
for i in range(900000,100000,-1):
    if iterseq(i)>max:
         max=iterseq(i)
         value=i
    print(str(i)+" and "+ str(max))
print("The longest Collatz chain is produced by "+ str(value)+"("+str(max)+")")

