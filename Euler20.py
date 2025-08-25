def factorial(number):
    if number==0 or number==1:
        return 1
    else:
        return number*factorial(number-1)

print("Welcome to the project Euler N°20: Factorial Digit Sum")
sum_digit=0
str_digit=str(factorial(100))
for i in range(len(str_digit)):
    sum_digit+=int(str_digit[i])
print("The sum of the digits in the number 100! is equal to : ", sum_digit)