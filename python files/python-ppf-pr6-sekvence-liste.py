osoba = ["Sofija", 25, "plava", False]

for x in range(len(osoba)):
    print(osoba[x])

for osobina in osoba: # skracena verzija
    print(osobina)

voce_i_povrce = ["jabuka","beli luk","crni luk","banana","mandarina","lubenica","krastavac"]

for stavka in voce_i_povrce:
    print(stavka)  # ovde se izlaze direktna vrednost
    
for i in range(len(voce_i_povrce)):  # ovde dobijemo i indeks i stavku
    print("Na indeksu: ",i,"nalazi se", voce_i_povrce[i])
    
for i, v in enumerate(voce_i_povrce):# kod enumerate moramo imati dve promenljive indeks i i vrednost v
    print("Indeks:",i,"Vrednost:", v)


automobili = ["Citroen", "BMW", "Opel", "KIA", "Jugo","Opel","Opel"]

for i,v in enumerate(automobili):
    print("Pozicija: ",i, "Automobil", v)
    
for i in range(len(automobili)):
    print("Pozicija: ",i, "Automobil: ",automobili[i])

for i,v in enumerate(automobili):
    if i == 1:
        print("Kupujem")
        
for pozicija, auto in enumerate(automobili):
    if auto =="Opel":
        print(pozicija, auto)

for pozicija, auto in enumerate(automobili):
    if len(auto) ==3:
        print(pozicija, auto)
        
# PROSIRENJE LSITE APPEND

automobili.append("Mercedes") # dodavanje novog clana u listu
automobili[2] ="Opel Corsa" # menjanje clana lsite 
automobili[3]="KIA Sportage"
print(automobili)

# BRISANJA CLANA LISTE - BRISANJE SA INDEKSIMA JE PRECIZNIJE A MOZE I BEZ NJIH U KOLIKO SMO SIGURNI DA IMAMO SAMO JEDNA CLAN SA TIM IMENOM
del automobili[3]
print(automobili)

automobili.remove("BMW") # BRISANJE SAMO PO VREDNOSTI
print(automobili)

automobili.pop(0) # TRECI NACIN BRISANJA
print(automobili)

broj_opela = 0

for indeks in range(len(automobili)):
    if automobili[indeks] == "Opel":
        print("Evo ga ope")
        broj_opela +=1

print("Imam ", broj_opela,"Opela na placu.")

# Brisanje svih clanova lsite i ostaje prazna lista.

automobili.clear()

print(automobili) 

# Slice-ovi

prazan_plac = []
#                 0        1       2      3       4       5        6
automobili = ["Citroen", "BMW", "Opel", "KIA", "Jugo","Peugeot","Audi"]

automobili_na_akciji = []

for i in range(len(automobili)):
    if i == 1 or i ==2 or i == 3:
        automobili_na_akciji.append(automobili[i])

print(automobili_na_akciji)

automobili_na_akciji = automobili[1:4] # slicevi

print(automobili_na_akciji)


automobili_na_akciji = automobili[1:4:2] # slicevi

print(automobili_na_akciji)

a = [3,7,1,9,2,4,5,12]

odd=[]
even=[]

for i in range(len(a)):
    if a[i] % 2 ==0:
        odd.append(a[i])
    else:
        even.append(a[i])

print(odd)
print(even)

brojevi = [1,10,12,7,3,4,2,5]

parni = []
neparni= []

for broj in brojevi:
    if broj % 2 ==0:
        parni.append(broj)
    else:
        neparni.append(broj)

print(parni)

print(neparni)

# ternarni operator

brojevi = [1,10,12,7,3,4,2,5]

parni = []
neparni= []

for broj in brojevi:
    parni.append(brojevi) if broj%2==0 else neparni.append(broj)

print(parni)

print(neparni)

