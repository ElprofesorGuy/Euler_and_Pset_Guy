def sumofsquare(lastnumber):
    return (lastnumber*(lastnumber+1)*((2*lastnumber)+1))/6

def squareofsum(lastnumber):
    sum=0
    for i in range(1,lastnumber+1):
        sum+=i
    return sum*sum

print("Welcome to the Project Euler N°6: Sum Square Difference.\n")
print("The sum difference beteween the sum of the squares of the first one natural numbers and the square of")
print(" the sum is: "+str(squareofsum(100))+"-"+str(sumofsquare(100))+"="+str(squareofsum(100)-sumofsquare(100)))