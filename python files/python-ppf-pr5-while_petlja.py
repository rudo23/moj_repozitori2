import random
sekunde = 10

while sekunde > 0:
    print(sekunde)
    sekunde -= 1
    
while False:
    print("Cao") 

baterija = 90

while baterija > 0:
    print("Mozes koristiti telefon.",baterija,"%")
    baterija -= random.randint(1,20)

print("Baterija je prazna")

