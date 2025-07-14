print("Welcome to the project Euler N° 2 : Even Fibonacci numbers.\n")
previous_fibonacci_term = 0
next_fibonacci_term = 1
sum = 0
while (next_fibonacci_term + previous_fibonacci_term)< 4000000:
    if (next_fibonacci_term+previous_fibonacci_term)%2==0:
        sum += next_fibonacci_term + previous_fibonacci_term
    print(str(sum) +"  "+ str(next_fibonacci_term+previous_fibonacci_term))
    temp = next_fibonacci_term
    next_fibonacci_term = previous_fibonacci_term + next_fibonacci_term
    previous_fibonacci_term = temp
    
print("The sum in the Fibonacci sequence whose values do not exceed 4000000 is equal to " + str(sum))