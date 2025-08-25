#ce rogramme calcule la somme des digits de a puissance a avec a compris entre 0 et 1001
print("Welcome to the project Euler N°48: Self Power.")
last_ten_digits = []
self_power=0
for int in range(1,1001):
    self_power+=int**int
self_power=list(str(self_power))
for i in range(len(self_power)-10,len(self_power)):
    last_ten_digits.append(self_power[i])
    
print("The last ten digits of the series is equal to :", ''.join(last_ten_digits))