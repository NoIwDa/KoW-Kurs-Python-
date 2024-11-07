import time
#notatki
#operacje numeryczne
# + dodawanie
# - odejmowanie
# * mnozenie
# / dzielene --> zwraca typ float
# // dzielenie --> zwraca typ integer
# %  modulo

# zmienna1 = 2
# zmienna2 = 10
# zmienna3 = 5
#
# print(f"dodanie {zmienna1} i {zmienna2} daje: ", str(zmienna1+zmienna2))
# print(f"odjecie od  {zmienna2} liczby {zmienna1} daje: ", str(zmienna2-zmienna1))
# print(f"pomnozenie {zmienna1} i {zmienna2} daje: ", str(zmienna1*zmienna2))
# print(f"dzielenie {zmienna2} przez {zmienna1} daje: ", str(zmienna2/zmienna1))
# print(f"dzielenie {zmienna2} przez {zmienna1} daje: ", str(zmienna2//zmienna1))
# print(f"reszta z dzielenia {zmienna3} przez {zmienna1} to: ", str(zmienna3%zmienna1))
#
# print(2%3)
#
#
# friends = 5
# print(f"Puchatek mial {friends} przyjaciol")
# friends = friends + 1
# print(f"A teraz ma {friends}")
#
# friends = 12
# print(f"\nPiotrus Pan mial {friends} przyjaciol")
# friends += 5
# print(f"A teraz ma {friends}")

#konwertowanie typow str() int() float() bool()

# name = "Harry Potter"
# name2 = "Ron"
# name3 = ""
# wiek = 12
# srednia_ocen = 4.1
# jest_uczniem = True
#
# print(type(name))
# print(type(wiek))
# print(type(srednia_ocen))
# print(type(jest_uczniem))
#
# name2 = bool(name2)
# print(name2)
# print(name3)
# name3 = bool(name3)
# print(name3)

#input
# hello = input("Jak masz na imie?\n")
# print(f"Witaj {hello}!")
# print("Typ danych wartosci hallo to: ", type(hello))
# age = input("Ile masz lat? \n")
# print(f"Masz {age} lat")
# print("Typ danych  age to: ", type(age))
# age = age + "1"
# age += "1"
# print(age)
# age1 = int(input("Ile masz lat? \n"))
# age1 +=1
# print(f"Wedlug systemu koreanskiego masz {age1} lat")

# wiek123 = int(input("Ile masz lat?\n "))
# czy_ma_bilet = False
# cena_biletu = 10
# print(f"Normalna cena biletu to: {cena_biletu}$")
#
# if wiek123 >=70:
#     print("Jestes seniorem")
#     print(f"Cena biletu ze znizka dla osob starszych to: {cena_biletu*0.5}$")
# elif wiek123 >= 18:
#     print("Jestes dorosly")
#     print(f"Cena biletu bez zadnej ulgi to: {cena_biletu}$")
#
# elif wiek123 < 0:
#     print("To ciekawe.")
# elif wiek123 ==0:
#     print("Bardzo ciekawe")
# else:
#     print("Jestes dzieckiem")
#     print(f"Cena biletu ze znizka dla dzieci to: {cena_biletu*0.7}$")
#
#
# if czy_ma_bilet:
#     print("Masz bilet \nYou shall pass ")
# else:
#     print("Nie masz biletu \nYou shall pass ")

# operacje logiczne
# or przynajmniej 1 warunek jest przwdziwy
# and wszystkie warunki musza byc prawdziwe
# not odwraca warunek (np not False

# temperatura = -100
# czy_pada = False
#
# if temperatura < -60 or temperatura > 60:
#     print("Chyba nadchodzi apokalipsa")
# elif temperatura < -1 or temperatura > 40:
#     print(" Dzis nie pora na przygode")
# elif temperatura > 35 and czy_pada == False:
#     print("Za cieplo na przygode")
# elif temperatura > 35 and czy_pada == True:
#     print("Za cieplo i mokro na przygode")
# elif temperatura < 35 and  temperatura > 20 and czy_pada == False:
#     print("Pora na przygode")
# elif temperatura < 35 and czy_pada == True:
#     print("Pora na przygode. Ale trzeba spakowac parasol!")


#
# czy_jest_slonecznie= False
# temperatura = 20
#
# if temperatura > 15 and  temperatura < 32 and not czy_jest_slonecznie:
#     print(" 1 Temperatura jest w sam raz, ale pada")
#
# czy_jest_slonecznie= True
# temperatura = 20
#
# if temperatura > 15 and  temperatura < 32 and not czy_jest_slonecznie:
#     print(" 2 Temperatura jest w sam raz, ale pada")

# petla while
#powtarza blok kodu tak dlugo jak postawiony warunek jest prawdziwy
#warunek jestponownie sprawdzany na koncu petli

#petla if wykonuje sie tylko raz
# if 1 ==1:
#     print("Ta petla jest nieskonczona  ∞ ")

# to samo, ale z petlahile

# while 1 == 1:
#     print("Ta petla jest nieskonczona  ∞ ")

# imie = input("Podaj imie")
#
#
# while imie =="":
#     imie = input("Podaj imie")
#
# wiek = int(input("Podaj Twoj wiek: "))
#
# while wiek <0 :
#     print("Wiek nie moze byc mniejszy od 0")
#     wiek = int(input("Podaj Twoj wiek: "))
#
# print(f"Witaj {imie}")
# print(f"Masz {wiek} lat")

#petla while jest idealna do sprawdzania inputu od uztkownika

#for loop dla string,list, tuple, set
#
# for i in range(10,0, -1):
#     print(i)

# name = "Pan Kleks"
#
# for letter in name:
#     print(letter)
#
# for letter in name:
#     print(letter, end=" ***")
#
# for i in range(10,0,-1):
#     print("Odliczanie: ",i)
#     time.sleep(1)
# print("Happy New Year!")

# Lista []
#  tuple ()
#  set {}

# lista_owocow = ["kiwi", "mandarynka", "wisnia"]
# lista_owocow[0] = "banan"
# lista_owocow.append("kiwi")
# for i in lista_owocow:
#     print(i, end=" ")
#
# print(lista_owocow)
# print(lista_owocow[0])
# print(lista_owocow[1])
# print(lista_owocow[2])
# print(lista_owocow[3])
#
# lista_owocow.remove("kiwi")
# print(lista_owocow)
# lista_owocow.reverse()
# print(lista_owocow)
# lista_owocow.pop(1)
# print(lista_owocow)

# nie da sie mdyfikowac zawartosci tuple

# tuple_owocow = ("kiwi", "mandarynka", "wisnia")

set1_owocow = {"kiwi", "mandarynka", "wisnia"}
set1_owocow.add("agrest")
set1_owocow.add("mango")
set1_owocow.add("gruszka")
print(set1_owocow)
set1_owocow.remove("wisnia")
print(set1_owocow)

owoc = input("Podaj jakiego owocu szukasz \n")

if owoc in set1_owocow:
    print(f"Ktos lubi {owoc} :D Mamy {owoc}")
else:
    print(f"Nie mamy {owoc} :(")
