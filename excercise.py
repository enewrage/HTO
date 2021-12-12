x = input("Podaj nazwę pliku tekstowego:")
plik = open(x).read()
count = len(open(x).readlines())
if count > 3:
    import linecache
    wiersz7 = linecache.getline(x, 7)
    print(wiersz7.replace("a", "z").replace("b", "w"))
    wiersz6 = linecache.getline(x, 6)
    print(wiersz6.replace("a", "z").replace("b", "w"))
    wiersz5 = linecache.getline(x, 5)
    print(wiersz5.replace("a", "z").replace("b", "w"))
if count < 3:
    print("Plik ma za mało linii.")
import linecache
wiersz1 = linecache.getline(x, 1)
wiersz2 = linecache.getline(x, 2)
wiersz3 = linecache.getline(x, 3)
nowy = open("wynik.txt","w")
nowy.write(wiersz1)
nowy.write(wiersz2)
nowy.write(wiersz3)
nowy.close()



