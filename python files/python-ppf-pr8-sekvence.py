# SORTIRANJE  RUCNO I AUTOMACKO

# brojevi = [9, 1, 3, 2, 5, 8, 7]

# brojevi.sort()
# print(brojevi)

# brojevi.reverse()

# print(brojevi)


brojevi = [9, 1, 3, 2, 5, 8, 7]
# od najmanjeg ka najvecem

# x  y
# privremeno mesto

for i in range(1, len(brojevi)):
    print(brojevi[i], "poredim sa",brojevi[i-1])
    
while True:
    izvrsena_zamena = False
    
    for i in range(1, len(brojevi)):
        if brojevi[i] < brojevi[i - 1]:                         # zamena pozicija brojeva ako je jedan veci od drugog BOOBLE SORT
            privremena = brojevi [i]
            brojevi[i] = brojevi[i-1]
            brojevi[i-1] = privremena
            izvrsena_zamena = True
    if izvrsena_zamena == False:
        break

print(brojevi)

proizvodi = ["Telefon", "TV", "Laptop"]
cene      = [  100,       200,    300 ]

for i in range(len(proizvodi)):
    print("Proizvod:",proizvodi[i],"-","Cena: ",cene[i])
    

automobili = ["Audi","Yugo" , "BMW", "Citroen", "Kia", "Peugeot"]

for i in range(len(automobili)):
    if  i == 3:
        print("Automobili: ", automobili[i])
        print("Pogodak ")
        


proizvodi = [
               ["iphone 11", "samsungs22","xiaomi x3"],# 0
               ["acer","macbook","dell"],# 1
               ["ipad", "samsung galaxy tab", "xiaomi tablet"]# 2
            ]

telefoni = ["iphone 11", "samsungs22","xiaomi x3"]
laptopovi = ["acer","macbook","dell"]
tableti = ["ipad", "samsung galaxy tab", "xiaomi tablet"]



print(proizvodi[0][0])
print(proizvodi[1][1])

# proizvodi = [telefoni, laptopovi, tableti]

# for kategorija in proizvodi:
#     for stavka in kategorija:
#         print(stavka)

for i in range(len(proizvodi)):
    print(proizvodi[i]) # i je prvi brojac
    for j in range(len(proizvodi[i])):
        print(proizvodi[i][j])  # j je drugi brojac
    

hrana = [
            ["cokolada","bombone","palacinke"],
            ["sarma", "musaka","kiseli kupus"],
            ["pecena paprika","ajvar","sopska"]
            
         ]

for kategorija in hrana:
    for jelo in kategorija:
        izlaz = f'''
        <div style ='border:1px solid red; background-color:gray;'>
            {jelo}"
        </div>
        
        '''
        print(izlaz)
# a = 10
# b = 15
# sabiranje = f"Sabiranje brojeva {a} i {b} je {a+b}"

biblioteka = [] # biblioteka se mora kreirati izvan while petlje jer ce se vjecno rekreirati nova prazna biblioteka u koliko se nalazi u while petlji.


while True:
    
    print("Odaberi komandu: 1- unos,2 - prikaz, 3 - brisanje, >3 izlaz")
    komanda = int(input("Unesite komandu: "))


    if komanda == 1:
        naslov = input("Unesite naslov: ")
        autor = input("Unesite autora: ")
        isbn = int(input("Unesite isbn: "))
        biblioteka.append([naslov, autor, isbn])
        print("Dodata knjiga")
    if komanda == 2:
        for knjiga in biblioteka:
            for detalj in knjiga:
                print(detalj)
    if komanda == 3:
        
        kljucna_rec = input("Unesite naslov knjige koju zelite obrisati: ")
        for knjiga in biblioteka:
            for detalj in knjiga:
                if detalj == kljucna_rec:
                    biblioteka.remove(knjiga)
                    print("Knjiga je obrisana")
    if komanda > 3:
        break
    
            