# number1 = int(input("Enter your first number: "))
# number2 = int(input("Enter your second number: "))

# print("Result is: ", number1 + number2)


# eur = 1.3
# usd = 1.1
# val=float(input("Enter value: "))

# total_euro = "Total Euro : %2f" % (val/eur)
# total_dollar = "Total Dollar: %2f" % (val/usd)

# print(total_euro)
# print(total_dollar)

# price = float(input("Enter price: "))
# tax = 0.2
# print("Price with tax is: ",price + price * tax)


# r = int(input("Enter radius: "))
# pi = 3.14
# print("Circle area is", r ** 2 * pi)

# amount = int(input("Enter amount: "))
# tens = amount // 10
# fives = (amount - (amount // 10) * 10) // 5
# two_s = (amount - (tens * 10) - (fives * 5)) // 2 
# ones = (amount - (tens * 10)-(fives * 5)-(two_s * 2))
# print("Tens : ", tens)
# print("Fives : ", fives)
# print("Two's : ", two_s)
# print("Ones : ", ones)

# number = int(input("Enter number : "))

# even_number = number % 2 == 0
# print("Number is even: ", even_number)

# import random

# racunar = random.randint(1,11)
# nas_broj = int(input("Enter number "))

# print("broj kompjutera", racunar)
# print("Nas broj ", nas_broj )

# pogodak = racunar == nas_broj

# print("Pogodak ", pogodak)

proj_x = 0
wall_x = 50
proj_spd = 10

print("Hit: ",proj_x > wall_x)
proj_x += proj_spd
print("Hit: ",proj_x > wall_x)
proj_x += proj_spd
print("Hit: ",proj_x > wall_x)
proj_x += proj_spd
print("Hit: ",proj_x > wall_x)
proj_x += proj_spd
print("Hit: ",proj_x > wall_x)
proj_x += proj_spd
print("Hit: ",proj_x > wall_x)
proj_x += proj_spd
print("Hit: ",proj_x > wall_x)
proj_x += proj_spd


# allowed_age = 13
# age = int(input("Enter your age: "))

# print("Allowed ",age >= allowed_age)


# db_username = "peter"
# db_password = "123"

# username = input("Enter username: ")
# password =  input("Enter password: ")

# print(db_password == password and db_password == password)


# x = 5
# y = 6
# sirina = 5
# visina = 4

# x1 = int(input("Enter x : "))
# y1 = int(input("Enter y : "))

# inZone = x1 >= x and x1 < x + sirina and y1 >= y and y1 < y + visina

# print("U zoni ste: ",inZone)


# number1 = int(input("Enter your first number: "))
# number2 = int(input("Enter your second number: "))

# result = number1 + number2
# print("Result is: ",result)

# eur = 1.3
# usd = 1.1

# vrednost = int(input("Unesite vrednost: "))
# total_euro = "Total Euro: %.2f " % (vrednost / eur)
# total_usd = "Total Dollar: %.2f " % (vrednost / usd)
# print(total_euro)
# print(total_usd)

# tax = 0.2
# price = float(input("Enter price: "))

# price_with_tax = price + (price * tax)
# print("Price with tax: ",price_with_tax)

# r = int(input("Enter radius: "))
# pi=3.14

# area = r ** 2 * pi
# print("Area is: ",area)

# amount = int(input("Enter amount: "))

# tens = amount // 10
# fives= (amount % 10) // 5
# twos = (amount % 10 % 5) // 2
# ones = (amount % 10 % 5 % 2)

# print("Tens: ", tens)
# print("Fives: ", fives)
# print("Two's: ", twos)
# print("Ones: ", ones)


# number = int(input("Enter number: "))

# even = number % 2 ==0

# print("Number is even: ", even)

# import random

# broj_korisnika = int(input("Unesite broj od 1 do 10: "))
# broj_kompjutera = random.randint(1,11)
# print("Broj kompjutera: ",broj_kompjutera)
# print("Broj korisnika: ",broj_korisnika)
# pogodak = broj_korisnika == broj_kompjutera
# print("Pogodak: ", pogodak)

# proj_x = 0
# wall_x = 50
# proj_spd = 10

# print("Pogodak: ",proj_x > wall_x)
# proj_x +=proj_spd + 10
# print("Pogodak: ",proj_x > wall_x)
# proj_x +=proj_spd + 10
# print("Pogodak: ",proj_x > wall_x)
# proj_x +=proj_spd + 10
# print("Pogodak: ",proj_x > wall_x)
# proj_x +=proj_spd + 10


# allowed_age = 13
# your_age = int(input("Enter your age: "))

# print("Allowed age: ",allowed_age <= your_age)


# db_username = "buro"
# db_password = "cuko"

# username = input("Enter username: ")
# password = input("Enter password: ")

# print(db_username == username and db_password == password)

x = 5
y = 6
sirina = 6
duzina = 7

x1 = int(input("Enter x: "))
y1 = int(input("Enter y: "))

uZoni = x1 >= x and x1< x + sirina and y1 >= y and y1 < y + duzina

print("U zoni ste: ",uZoni)
