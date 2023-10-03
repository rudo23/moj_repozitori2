#           0       1      2      3       
osoba = ["Sofija", 20, "plava", True] # lista ili niz 

print("Ime:", osoba[0])
print("Godine:", osoba[1])
print("Boja kose:", osoba[2])
print("Slobodna:",osoba[3])


automobili =["OPEL","CITROEN","MERCEDES"]
print(automobili[1])


for x in range(10):
    print(x)

for x in range(5,10):
    print(x)

for x in range(5,10,2):
    print(x)
    
    
       #012345
kurs = "python"

print(kurs[0])
print(kurs[1])
print(kurs[2])
print(kurs[3])
print(kurs[4])
print(kurs[5])


for x in range(6):
    print(kurs[x])
    
for x in range(len(kurs)): # len je funkcija koja broji broj clanova sekvence koja joj se prosledi u zagradi.
    print("Na poziciji: ",x, kurs[x])

duzina = len(kurs)  

for x in range(duzina):
    print("On position: ",x, kurs[x])
    

ustanova = "IT Academy"

for x in range(len(ustanova)):
    print("NA INDEKSU:",x,ustanova[x])


primer = "zadatak1"

for index in range(len(primer)):
    print(primer[index],end="") # end moze svuda i sluzi da se sve zadrzi u istom redu

print()
# prolazak kroz sekvencu pomocu while petlje  
    
broj_karaktera = len(primer)
print(broj_karaktera)
indeks=-1

while indeks < broj_karaktera:
    print(primer[indeks])
    indeks +=1

# operacije stringa NAJCESCE LOWER I UPER

# korisnicko_ime = "admin"
# uneto_korisnicko_ime = input("Unesi korisnicko ime: ").lower()

# if korisnicko_ime == uneto_korisnicko_ime.lower(): 
#     print("Dobrodosli")
# else:
#     print("Pogresni podaci")
racunar = "laptop"
model = "mackbook"
racunar[1]= "C"  # vraca gresku jer je string ne mutabilan
racunar + model # spajanje dva stringa
racunar = "desktop" # ovde ne menjamo string vec menjamo adresu an koju se nalazi i koristi se u daljem kodu ovaj koji je noviji

racunar = "laptop"

print(racunar.capitalize())