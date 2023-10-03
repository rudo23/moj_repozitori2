# for while

for x in range(1,7): # spoljnja for funkcija ne crta nista sam obroji redove
    for y in range(5):
        print("#",end = " ")
    print("Novi red") # print() enter daje to da sve prejde u novi red


for x in range(10):
    for y in range(10):  
        if y > x:
            print("#",end="")
        else:
            print("",end ="")  # dva potpuno drukcija trougla zbog space u praznom stringu
    print()
        


for x in range(10):
    for y in range(10):
        if y > x:
            print("#",end=" ")  # razmak u end="" ili end=" " space bass puno utice na ove trouglove
        else:
            print(" ",end =" ") # dva potpuno drukcija trougla zbog space u praznom stringu
    print()
    

automobil = 0
cilj = 100
brzina = 10

gorivo = 10

while automobil < cilj:
    print("Voznja je u toku.")
    automobil += brzina
    gorivo -= 5 
    if gorivo ==0:
        print("Nemate goriva")
        break
else:
    print("Stigli ste.")

print("U svakom slucaju.")


        


         