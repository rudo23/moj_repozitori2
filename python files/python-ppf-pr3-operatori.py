import random

kurs = "Python Fundamentals"
print(kurs)
# OPERATOR DODELE JE ZNAK = !!!!!!!!!!!!!!!!!!!!!!! ZATO IDE += 1  
a = 10
b = 5

print(a + b)

rezultat_sabiranja= a + b
print(rezultat_sabiranja)

print("Oduzimanje:",a - b)
print("Mnozenje:",a * b)
print("Deljenje:", a / b)

print("Celobrojno deljenje: ", a // b)
print(10 // 3)
print(10 / 3)

print(a ** 2) # a * a
print(a ** 3) # a * a * a

# 10 / 3 = 3
# 3 * 3 = 9
# 9 + 1 = 10

print(10 % 3) # koristi se kada zelimo da proverimo da li je broj paran ili ne --ako nema ostatak kada se deli sa 2 onda je paran.
print(5 % 2)
print(8 % 2)

print(-a) # unarni operator
# a=(-a)
print(a)

godine = 25
# GODINE + 1

godine = godine + 1

godine += 1 # znak += znaci uvecavam i dodeljujem

print(godine)

godine -= 5
print(godine)

godine *= 2
print(godine)

godine /=2
print(godine)

godine //= 2
print(godine)

# broj1 = 15
# broj2 = 20

# print("Zbir:", broj1 + broj2)

# broj1= int(input("Unesite broj jedan : "))
# print(broj1)

# broj2= int(input("Unesite broj dva: "))
# print(broj2)

# print(f"Rezultat je : {broj1} + {broj2} = {broj1+broj2}")

# suma = float(input("Unesite zeljenu sumu :"))

# kurs_eur = 1.3
# kurs_usd = 1.1

# konverzija_eur = suma * kurs_eur
# konverzija_usd = suma * kurs_usd

# print("Iznos sume konvertovane u eurima je : ", konverzija_eur)
# print("Iznos sume konvertovane u usd je: ", konverzija_usd)

# poluprecnik = float(input("Unesite poluprecnik: "))
# pi = 3.14

# povrsina = poluprecnik ** 2 * pi
# print("Povrsina kruga je: ", povrsina)

# unos = input("Unesi nesto:...")

# print(unos.isnumeric())

# print(10 ** 3)

stara_kilaza = 80
nova_kilaza = 99

print(stara_kilaza > nova_kilaza)
print(stara_kilaza < nova_kilaza)

print(nova_kilaza == 100)
print(nova_kilaza != 100)
print(stara_kilaza >= 80)

username = "test"
password = "abc123" 

print(username == "test")
print(password == "abc123")

godine = 20
print(godine >= 16)

# broj = int(input("Enter number: "))

# provera = broj % 2

# print("Paran broj?",provera == 0)



# korisnik=int(input("Unesite broj od 1 do 10: "))
# racunar=random.randint(1,11)

# print("Korisnik: ", korisnik)
# print("Racunar: ", racunar)
# print("Pogodak: ", korisnik == racunar)


automobil = 0
cilj = 50

print(automobil >= cilj)
automobil += 10
print(automobil >= cilj)

automobil += 20
print(automobil >= cilj)

automobil += 25
print(automobil >= cilj)


provera_imena = True # ime == sacuvano_ime
provera_sifre = False # sifra == sacuvana_sifra

print(provera_imena and provera_sifre)

'''
and

true true -> true
false true -> false
true false -> false
false false -> false


or

true true -> true
true false -> true
false true -> true
false false -> false


not 

true -> false
false -> true

'''
lepo_vreme = False
print(not lepo_vreme) # logicki operator not pretvara u suprotnu vrednost 

x = 10
y = 15
print(x is y)


smer = input("Unesite smer: ")
godina = int(input("Unesite godinu upisa: "))

odobreno = smer == "python" and godina == 2022

# provera_smer = smer == "python"
# provera_godina = godina == 2022
# odobreno = provera_smer and provera_godina

print(odobreno)
















