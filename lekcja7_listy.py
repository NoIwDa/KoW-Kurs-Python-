#co to jest lista?
#lista to pudelko do wkladamy wiele roznych wartosci ktore moga byc roznego rodzaju (int, str, bool) i ktore moga sie powtarzac
#lista jest oznaczona nawiasami kwadratowymi [] a poszczegolne elementy sa oddzielane od siebie przecinkiem
#elementy w liscie sa indeksowane od zera
#utwozona raz lise mozna dowolnie modyfikowac
lista = ["jeden", 2, "jeden",3,4,True]
print(lista)
lista1 = ["jeden","dwa","trzy","cztery","piec", True,]
#python pozwala na urzywanie przecinku na koncu, za ostanim elemencie listy
#nie jest to konieczne
lista2 = [1,2,3,4,5, True]
#oba zapisy sa poprawne
print("Lista 1: ",lista1)
print("Lista 2: ",lista2)
print("Wyswietlanie wszystkich elementow z listy 1 przez wypisanie"
      " indeksu: \n", lista1[0] ,lista1[1],lista1[2],lista1[2],lista1[4],lista1[5])
print("Wymieszanie co 1 elementow z list 1 i 2. Elementy sa "
      "wypisane w ten sam sposob co poprzednio: \n", lista1[0], lista2[1], lista1[2], lista2[2], lista1[4],lista2[5])


tekst = "Ksiezyc Europa"
print(tekst[0])
print(tekst)
for i in tekst:
      print(i)

print(tekst + "jest wyjatkowy")

print("To sa lista1 i lista2: ",lista1 + lista2, "\n to tylko wyswietla je razem")
print(lista2 + ["g","hhhh"])
print(lista2) #zawartosc listy2 sie niezmienila bo nic nowego do niej nie przypisano. Jedynie wydrukowano jej istniejaca wartosc
                                                                                      # z dodatkowymi elementami do druku
print(lista1 *3)

print("Zmierzmy dlugosc list. Dlugosc listy to: ", len(lista))
print("Zmierzmy dlugosc list. Dlugosc listy1 to: ", len(lista1))
print("Zmierzmy dlugosc list. Dlugosc listy2 to: ", len(lista2))

lista1.append("czesc, wpadlam do listy")
print("Zobaczmy zmiany: \n", lista1)
print("Zmierzmy dlugosc list. Dlugosc listy1 to: ", len(lista1))
lista1.insert(0, "Tez wpadlo mi sie do listy :D")
print("Spradzmy zmiany: \n", lista1)
lista1.append("jeden")
print("Spradzmy zmiany: \n", lista1)
lista1.insert(1,"jeden")
print("Spradzmy zmiany: \n", lista1)
print("Ilosc 'jeden' w lista1: ", lista1.count("jeden"))
print("Lista2: ", lista2)
print("Policz 1 w lista2: ", lista2.count(1))
#wartosc logiczna True zwracana jest jako 1latego lista2.count(1) zwraca 2 pomimo ze w liscie jest tylko jedna 1, wartosc True jest zliczona jako '1'
print("Policz 2 w lista2: ", lista2.count(2))
lista2.append(False)
print(lista2)
print(lista2.count(0))
# w ten sam sposob dziala wartosc False

#potencjalne bledy : IndexError out of range --> podany indeks nie jest elementem listy/lista ma indeksy od 0 do 9 a dano np. 11

lista_false = [False, False, False,0, False]
print(lista_false.count(False))