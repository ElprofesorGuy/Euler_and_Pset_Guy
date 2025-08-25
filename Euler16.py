print("Welcome to the project Euler N°16: Power Digit Sum\n")
sum_digit=0
str_digit=str(2**1000)
print(str_digit)
for i in range(len(str_digit)):
    sum_digit+=int(str_digit[i])
print(sum_digit)