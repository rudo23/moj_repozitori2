import random
tiket = []
ulog =int(input("Unesite ulog : "))
while  range(len(tiket)< 3): 

    utakmica = int(input("Unesite sifru  zeljene utakmice (300,301,302) : "))
    
    utakmica1 = "Manchester United vs Chelsea"
    utakmica2 = "Leeds United vs Liverpool"
    utakmica3 = "Barcelona vs Real Madrid"

    if utakmica == 300:
        print(utakmica1)
        tip1 = int(input("Unesite tip (1,0,2) "))
        tiket.append(utakmica1)
        kvota1 = 2.35
        kvota0 = 3.00
        kvota2 = 3.55
        
        if tip1 == 1:
            dobitak1 = ulog * kvota1
        elif tip1 == 0:
            dobitak1 = ulog * kvota0
        else:
            dobitak1 = ulog * kvota2
        man_united = random.randint(1,5)
        chelsea = random.randint(1,3)
        rezultat1 = []
        if tip1 != 1 and tip1 != 0 and tip1 !=2:
            print("Greska pokusajte ponovo")
            tiket.pop(0)
        
        elif man_united > chelsea and tip1 == 1:
            print("Pogodak kvota", kvota1)
            print("Rezultat: ","Manchester United",man_united ,"vs","Chelsea", chelsea)
            rezultat1.append(1)
        elif man_united == chelsea and tip1 == 0:
            print("Pogodak kvota ", kvota0)
            print("Rezultat: ","Manchester United",man_united ,"vs","Chelsea", chelsea)
            rezultat1.append(1)
        elif man_united < chelsea and tip1 ==2:
            print("Pogodak kvota ", kvota2)
            print("Rezultat: ","Manchester United",man_united ,"vs","Chelsea", chelsea)
            rezultat1.append(1)
        else:
            print("Promasaj")
            print("Rezultat: ","Manchester United",man_united ,"vs","Chelsea", chelsea)
            rezultat1.append(2)
         
    elif utakmica == 301:
        print(utakmica2)
        tip2 = int(input("Unesite tip (1,0,2) "))
        tiket.append(utakmica2)
        kvota1 = 5.60
        kvota0 = 3.00
        kvota2 = 1.55
        if tip2 == 1:
            dobitak2 = ulog * kvota1
        elif tip2 == 0:
            dobitak2 =ulog * kvota0
        else:
            dobitak2 = ulog * kvota2
        leeds = random.randint(1,2)
        liverpool = random.randint(1,6)
        rezultat2 = []
        
        if tip2 != 1 and tip2 != 0 and tip2 !=2:
            print("Greska pokusajte ponovo")
            tiket.pop(0)
     
        elif leeds > liverpool and tip2 == 1:
            print("Pogodak kvota", kvota1)
            print("Rezultat: ","Leeds United ",leeds ,"vs","Liverpool", liverpool)
            rezultat2.append(1)
        elif leeds == liverpool and tip2 == 0:
            print("Pogodak kvota ", kvota0)
            print("Rezultat: ","Leeds United ",leeds ,"vs","Liverpool", liverpool)
            rezultat2.append(1)
        elif leeds < liverpool and tip2 ==2:
            print("Pogodak kvota ", kvota2)
            print("Rezultat: ","Leeds United ",leeds ,"vs","Liverpool", liverpool)
            rezultat2.append(1)
        else:
            print("Promasaj")
            print("Rezultat: ","Leeds United",leeds ,"vs","Liverpool", liverpool)
            rezultat2.append(2)
            
    elif utakmica == 302:
        print(utakmica3)
        tip3 = int(input("Unesite tip (1,0,2) "))
        tiket.append(utakmica3)
        kvota1 = 1.75
        kvota0 = 3.00
        kvota2 = 6.50
        if tip3 == 1:
            dobitak3 = ulog * kvota1
        elif tip3 == 0:
            dobitak3 =ulog * kvota0
        else:
            dobitak3 = ulog * kvota2
        
        barcelona = random.randint(1,6)
        real_madrid = random.randint(1,3)
        
        rezultat3 = []
        
        if tip3 != 1 and tip3 != 0 and tip3 !=2:
            print("Greska pokusajte ponovo")
            tiket.pop(0)
        
        elif barcelona > real_madrid and tip3 == 1:
            print("Pogodak kvota", kvota1)
            print("Rezultat: ","Barcelona ",barcelona,"vs","Real Madrid", real_madrid)
            rezultat3.append(1)
        elif barcelona == real_madrid and tip3 == 0:
            print("Pogodak kvota ", kvota2)
            print("Rezultat: ","Barcelona ",barcelona ,"vs","Real Madrid", real_madrid)
            rezultat3.append(1)
        elif barcelona < real_madrid and tip3 ==2:
            print("Pogodak kvota ", kvota2)
            print("Rezultat: ","Barcelona ",barcelona ,"vs","Real Madrid ", real_madrid)
            rezultat3.append(1)
        else:
            print("Promasaj")
            print("Rezultat: ","Barcelona ",barcelona ,"vs","Real Madrid", real_madrid)
            rezultat3.append(2)
    else:
        print("Pogresan unos proverite sifru meca (300,301,302)")
        

kvota = (dobitak1/ ulog) * (dobitak2/ ulog) * (dobitak3/ulog)
print("Ukupna kvota: %.2f " % (kvota))
print("Ulog:",ulog)
print("Moguci dobitak %.2f " % (kvota * ulog))

rezultat_1 = int("".join(map(str, rezultat1)))
rezultat_2 = int("".join(map(str, rezultat2)))
rezultat_3 = int("".join(map(str, rezultat3)))

if rezultat_1 != 1 or rezultat_2 != 1 or rezultat_3 != 1:
    print("Tiket je gubitan")
else:
    print("Dobitni tiket")

print("Par: ", tiket[0], "tip", tip1,"kvota %.2f " % (kvota/(dobitak2/ulog)/(dobitak3/ulog)))
print("Par: ", tiket[1], "tip", tip2,"kvota %.2f " % (kvota/(dobitak1/ulog)/(dobitak3/ulog)))
print("Par: ", tiket[2], "tip", tip3,"kvota %.2f " % (kvota/(dobitak1/ulog)/(dobitak2/ulog)))
