
pozicija_automobila = 0
pozicija_cilja = 10

pozicija_automobila += 2
print(pozicija_automobila == pozicija_cilja)

pozicija_automobila += 2
print(pozicija_automobila == pozicija_cilja)

pozicija_automobila += 2
print(pozicija_automobila == pozicija_cilja)

pozicija_automobila += 2
print(pozicija_automobila == pozicija_cilja)

pozicija_automobila += 2
print(pozicija_automobila == pozicija_cilja)

for ime in ["marko","milos","marija","sofija","ana"]:
    print("Hello!", ime)

print("Prva sledeca linija.....")

for broj in [1, 2, 3, 4, 5]:  # range ili opseg   range(1,20)-ovo je redom od 1 do 19 ne obuhvata zadnji broj ---  range(1,20,2) od 1 do 20 ali ide svak idrugi broj
    print("Ovo je broj: ", broj)
    
for broj in range(1,21):
    print("Stampanje broja",broj)

for broj in range(21):           # kada je samo jedan broj onda pocinje od 0 do tog broja al ne uzima zadnji broj.
    print("Ovo je broj", broj)
    
for broj in range(5,10,2):
    print("broj:",broj) # brojanje ide od 5 do 10 al se brojevi povecavaj uza dva-- to oznacava treci broj.
    
for broj in range(100,0,-1): # kada ocemo da ide u nazad moramo staviti 3 broj i to -1
    print("Prikaz",broj)
    
pozicija_automobila = 0
pozicija_cilja = 10

for trenutna_pozicija in range (pozicija_cilja + 1):
    pozicija_automobila = trenutna_pozicija
    print(pozicija_automobila == pozicija_cilja)


print("*******************Allowed years***************************")
for years in range(2010,2016):
    print(years)
    
print("***********************************************************")


print("*************************Years*****************************")
pocetna_godina=2010
zavrsna_godina=2021

for godina in range(pocetna_godina,zavrsna_godina):
    print(godina)
print("***********************************************************")

for zvezda in range(0,100):
    print("*",end="") # End sprecava da zvezdice odu u novi red i sve ostaju u njemu zbog toga.

print()

 # \ jeste zamena za tab
# print("Ovo je kurs \"Python\" ") # kada zelimo da nam tekst printa sa dvostrukim navodnicima
# print("Ovo je deljenje, delim brojeve: a\\b") # kada zelimo u ispisu da koristimo \, moramo koristiti dva takva jer jedan ce od karaktera do sebe napraviti specijalan karakter.

# broj = int(input("Unesi broj: "))
# print("1\t2\t3\t")
# print("********************")

# for brojac in range(1,broj + 1):
#     print(brojac * 1, end ="\t")
#     print(brojac * 2, end ="\t")
#     print(brojac* 3, end ="\n")


# for x in range(5):
#     for y in range(3):
#         print("Ovo je x:", x,"Ovo je y:", y)


# print() # enter se ovako pise u pythonu

for x in range(6):
    for y in range(6):
        print("*",end=" ")
    print() # enter da sve ne bi islop u novi red

for x in range(6):
    for y in range(x-1):     
        print("*",end=" ")
    print()
for x in range(7):
    for y in range(6-x-1):
        print("*",end=" ")
    print()


for x in range(6):
    for y in range(x-1):
        print("*",end=" ")  # trokut
    print()

for x in range(6):
    for y in range(6):
        if x==y:
            print("*",end=" ")
        else:
            print("#",end=" ")
    print()
    

for x in range(6):
    for y in range(6):       # ternarni operator skracuje kod
        print("*",end=" ") if x==y else print("#",end=" ")
    print()


for x in range(6):
    for y in range(6):
        if x==0 or x==5 or y==0 or y==5:
            print("#",end=" ")
        else:
            print(" ",end=" ")
    print()


for x in range(10):
    for y in range(10):
        if x==0 or x==9 or y==0 or y==9:
            print("#",end=" ")
        else:
            print(" ",end=" ")
    print()
    
# prekini petlju kad naidjes na broj 5
    
for broj in range(1,11):
    if broj == 5:
        break
    print("Redni broj: ", broj)
    

# stampaj sve brojeve osim broja 2

for brojevi in range(0,11):
    if brojevi == 2:
        continue
    print("Redni broj ", brojevi)