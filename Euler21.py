def sum_of_divider(number):
    sum=0
    for c in range(1,int(number/2)+1):
        if number%c==0:
            sum+=c
    return sum

print("Welcome to the project Euler N°21: Amicable Numbers")
Amicable_sum=0
b=0
c=0
for a in range(2, 10000, 1):
   b=sum_of_divider(a) 
   c=sum_of_divider(b)
   if c == a and a!=b:
       Amicable_sum+=a
print("The sum of all the amicable numbers under 10000 is equal to : ", Amicable_sum)
