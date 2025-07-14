def isprimenumber(number):
    counter = 1
    for divider in range(2,number+1):
        if number%divider == 0:
            counter+=1
        if counter == 2:
            break
    if divider != number:
        return False
    else:
        return True

order = 0
number = 1
while order != 10001:
    number+=1
    if isprimenumber(number):
        order+=1
print("The 10001st prime number is "+ str(number))