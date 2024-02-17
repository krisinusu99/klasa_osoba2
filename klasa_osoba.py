class Osoba: # Klasa osoba.
    def __init__(self): # Metoda __init__
        print("Obiekt klasy Osoba zosta utworzony.")
        print()
        print("Wprowadzanie danych do programu.")
        print()
    def __del__(self): #Metoda __del__
        print()
        print("Obiekt klasy Osoba zosta usuniety")
        print("Zakonczenie programu=")
    def czytaj_dane(self):
        self.nazwisko=input("Podaj nazwisko")
        self.imie=input("Podaj imie")
        self.ulica=input("Podaj ulice")
    def wyswietl_dane(self):
        print()
        print("Wyprowadzanie danych z programu")
        print()
        print("Nazwisko:",self.nazwisko,".",sep="")
        print("Imie:",self.imie,".",sep="")
        print("Ulica:",self.ulica,".",sep="")
def main():
    Pracownik=Osoba()

    Pracownik.czytaj_dane()
    Pracownik.wyswietl_dane()
    del Pracownik
main()