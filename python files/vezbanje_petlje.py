import time

# start_date = 2010
# end_date = 2016
# print("****************************Allowed years **********************************")
# for years in range(start_date,end_date):
#     print(years)
# print("****************************************************************************")


# # broj =int(input("Unesite broj: "))

# # print("1\t2\t3\t")
# # print("*********************************************")

# # for brojac in range(broj):
# #     print(brojac * 1, end="\t")
# #     print(brojac * 2, end="\t")
# #     print(brojac * 3, end="\n")

# w = 10
# h = 5

# for x in range(h):
#     for y in range(w):
#         if x==0 or x==h-1 or y==0 or y==w-1:
#             print("#",end=" ")
#         else:
#             print(" ",end=" ")
#     print()
    
    

# h = 10

# for i in range(h):
#     for y in range(i-1):
#         print("#",end="")
#     print()

# h = 10

# for i in range(h):
#     for y in range(i-1):
#         print("#",end="")
#     print()

# for i in range(h):
#     for y in range(h-i-1):
#         print("#",end="")
#     print() 
    
# h = 10

# for x in range(h):
#     for  y in range(h):
#         if x>y:
#             print(" ",end=" ")
#         else:
#             print("*",end=" ")
#     print()
            

# n = int(input("Enter the number of rows: "))

# for i in range(n):
#     for j in range(n-i-1):
#         print(" ",end="")
#     for j in range(2*i+1):
#         print("*",end="")
#     print()
        

# startDate = 2010
# endDate = 2015

# print("**********************Allowed Years**************************")
# for year in range(startDate,endDate + 1):
#     print(year)
# print("*************************************************************")


# broj = int(input("Unesite broj: "))

# for brojac in range(broj):
#     print(brojac * 1 ,end="\t")
#     print(brojac * 2 ,end="\t")
#     print(brojac * 3 ,end="\n")
    

# w=10
# h=5

# for x in range(h):
#     for y in range(w):
#         if x == 0 or x == h-1 or y == 0 or y == w-1:
#             print("*",end ="")
#         else:
#             print(" ",end="")
#     print()
    

# h= 10

# for i in range(h):
#     for j in range(i-1):
#         print("*",end="")
#     print()

# h= 10

# for i in range(h):
#     for j in range(i-1):
#         print("*",end="")
#     print()
# h= 10

# for i in range(h):
#     for j in range(h-i-1):
#         print("*",end="")
#     print()

# h = 10

# for i in range(h):
#     for j in range(h+1):
#         if j>i:
#             print("*",end="")
#         else:
#             print(" ",end="")
#     print()   
    

# h = 10

# for i in range(h):
#     for j in range(h-i-1):
#         print(" ",end="")
#     for j in range(2*i+1):
#         print("*",end="")
#     print()     




# x = 0
# cilj = 50

# for i in range(cilj):
#     for j in range(cilj):
#         if j == x:
#             print("#",end="")
#         else:
#             print(" ",end="")
#     x+=1
#     print("\r",end="")
#     time.sleep(0.1)
    
    
# meta = 50
# metak=0

# for x in range(meta):
#     for y in range(meta):
#         if y == metak:
#             print("->",end="")
#         else:
#             print(" ",end="")
#     metak+=1
#     print("\r",end="")
#     time.sleep(0.3)
    


# strela = 0
# meta = 50

# for x in range(meta):
#     for y in range(meta):
#         if y == strela:
#             print("-->",end="")
#         else:
#             print(" ",end="")
#     strela+=1
#     print("\r",end="")
#     time.sleep(0.3)
    
# sabiranje = 0
# while True:
#     broj = input("Unesi broj: ")
#     if broj == "":
#         print("Rezultat", sabiranje)
#     else:
#         if broj.isnumeric():
#             sabiranje+=int(broj)
#         else:
#             print("Vrijednost nije numercika, unesite numericku vrednost: ")
            
# sabiranje = 0
# while True:
             
    
#     broj = input("Unesi broj: ")
    
#     if broj == "":
#         print("Rezultat sabiranja: ",sabiranje)
#     else:
#         if broj.isnumeric():
#             sabiranje += int(broj)
#         else:
#             print("Pogresan unos, unesite numericku vrednost. ")
    
# import time

# meta = 50
# x = 0

# for x in range(meta):
#     for y in range(meta):
#         if y == x:
#             print("\-->",end="")
#         else:
#             print(" ",end="")
#     print("\r",end="")
#     x+=1
#     time.sleep(0.2)

start_date = 1994
end_date = 2024

for years in range(start_date, end_date):
    print("Godina: ",years)


# broj = int(input("Unesite broj: "))

# print("1\t2\t3\t")
# print("******************")

# for brojac in range(broj):
#     print(brojac * 1,end="\t")
#     print(brojac * 2,end="\t")
#     print(brojac * 3,end="\n")


# w = 10
# h = 5

# for x in range(h):
#     for y in range(w):
#         if x==0 or x ==h-1 or y == 0 or y == w-1:
#             print("#",end="")
#         else:
#             print(" ",end="")
#     print()


# h = 10

# for i in range(h):
#     for j in range(i+1):
#         print("*",end="")
#     print()


# h = 10

# for i in range(h):
#     for j in range(i - 1):
#         print("*",end="")
#     print()

# h = 10

# for i in range(h):
#     for j in range(h - i - 1):
#         print("*",end="")
#     print()


# h = 10

# for x in range(h):
#     for y in range(h):
#         if y>x:
#             print("#",end="")
#         else:
#             print(" ",end="")
#     print()

# h = 10

# for x in range(h):
#     for y in range(h-x-1):
#         print(" ",end="")
#     for y in range(2*x+1):
#         print("*",end="")
#     print()


# meta = 50
# strela = 0

# for x in range(meta):
#     for y in range(meta):
#         if y == strela:
#             print("|=>",end="")
#         else:
#             print(" ",end="")
#     print("\r",end="")
#     strela +=1
#     time.sleep(0.2)
sabiranje = 0
while True: 
    broj = input("Unesite broj: ")
    
    if broj == "":
        print("Rezultat sabiranja", sabiranje)
    else:
        if broj.isnumeric():
            sabiranje +=int(broj)
        else:
            print("Unesena vrednost nije broj, pokusajte ponovo. ")
     
        
        
        

