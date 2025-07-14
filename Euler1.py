print("Welcome to the project Euler N°1");
sum_multiple=0
for i in range(3,1000):
    if i%3==0 or i%5==0:
        sum_multiple+=i
print(sum_multiple)