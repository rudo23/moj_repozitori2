import random


x = -10

if x > 0:
    print("Broj je pozitivan")
    
print("Izvrsava se u svakom slucaju")






vozilo_u_pokretu = True
brzina = 60

if vozilo_u_pokretu == True:
    print("Vozilo se krece...")
    print("Proverite i brzinu...")
    if brzina > 50:
        print("Prekoracena brzina")
    print("Ovo izvrsavam kolika god da je brzina")
    if brzina <= 50:
        print("Brzina je OK.")

if vozilo_u_pokretu == False:
    print("Vozilo se ne krece...")
    
#1 - prikaz :2 - kupovina : 3 - izlaz
# proizvod = "duks"
# cena=3000

# komanda = int(input("Unesite zeljenu opciju: "))

# if komanda == 1:
#     print("Prikazi proizvode")
#     print("Proizvod:", proizvod,"Cena:", cena)
# if komanda == 2:
#     print("Kupovina proizvoda")
#     stanje = int(input("Unesite stanje na racunu: "))
#     if stanje >= cena:
#         print("Uspjesna kupovina, preostalo na racunu:", stanje - cena)
#     else:
#         print("Neuspesna transakcija")
# if komanda == 3:
#     print("Izlaz")

broj = 5

if broj > 0:
    print("Broj je veci od 0.")
else:
    print("Broj je 0 ili manji od 0.")
marija = False
ksenija = True
katarina = False


devojka_na_dejtu = ""

if marija:
    devojka_na_dejtu = "marija"
elif  katarina:
    devojka_na_dejtu = "katarina"
elif ksenija:
    devojka_na_dejtu = "ksenija"
else:
    devojka_na_dejtu = "sofija"
    
print("Izlazi sa mnom:",devojka_na_dejtu) 

automobil_polovan = False
godiste = 2021
boja = "crna"

if  (automobil_polovan == True or godiste > 2017) and boja=="crna":
    print("Kupujem")

if not automobil_polovan:
    print("Automobil je nov.")
    
prisutan = False # nije na casu
smer = "python"

if prisutan  and smer == "python": # if prisutan znaci da li je prisutan == True a if not prisutan znaci da li je false i if prisutan == False
    print("Polaznik je bio na casu")
        
if prisutan == True:
    print("Na casu je")
    
if not prisutan: # ako nas interesuje da li je nesto false
    print("Nije na casu")

# high_score = random.randint(1,101)
# your_score = int(input("Enter your score : "))

# if your_score > 100 or your_score <1:
#     print("Check your number, number is out of range(1-100)")
# elif your_score > high_score:
#     print("Congrats! You beat the high score",high_score)
#     print("Highscore:", your_score)
# elif high_score == your_score:
#     print("Your tied high score")  
# else:
#     print("You need to train more.", high_score) # svi printovi moraju biti u istoj liniji kod ovakvog koda

# ternarni operatori

# pol = input("Unesite pol: ")
# poruka = ""

# if pol == "m":
#     poruka = "Hey mister!"
#     print(poruka)
# else:
#     poruka = "Hey miss!"
#     print(poruka)
    
# # ternarni operator za skracivanej koda.
# poruka = "Hey mister!" if pol == "m" else "Hey miss!"

# print(poruka)

popularan_proizvod = ""
jesen = False  

if jesen:
    popularan_proizvod = "Jabuke"
else:
    popularan_proizvod = "Sladoled" 

print(popularan_proizvod)

# terarni operator
popularan_proizvod = "Jabuke" if jesen  else "Sladoled"
print(popularan_proizvod)







    
          



    
    

