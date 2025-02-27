""" Představ si situaci, že chceš napsat takový program, který ti umožní rezervovat jízdenky.

Samozřejmě nepůjde o žádnou produkční verzi ale jednoduchý skript postavený na komunikaci uživatele a interpretu.


Program bude umět:

Pozdravit uživatele,
Vypsat nabídku,
Dovolit uživateli zadat vstupní data,
Zpracovat vstupní data,
Vypsat zpracovaná data. """

mesta = ["Praha", "Viden", "Olomouc", "Svitavy", "Zlin", "Ostrava"]
ceny = (150, 200, 120, 120, 100, 180)
cara = "=" * 35
nabidka = """1 - Praha   | 150
2 - Viden   | 200
3 - Olomouc | 120
4 - Svitavy | 120
5 - Zlin    | 100
6 - Ostrava | 180"""

print("VITEJTE U NASI APLIKACE DESTINATIO!")
print(cara)
print(nabidka)
print(cara)
cityChoice = (int(input("Zadejte číslo destinace:" + " ")))
firstName = input("Jméno:")
surname = input("Příjmení:")
mail = input("Email:")
print(cara)
cityChoice = cityChoice - 1
cityName = mesta[cityChoice]
realPrice = ceny[cityChoice]
print("Jméno:", firstName)
print("Příjmení:", surname)
print("Email:", mail)
print("Vybrané město je" + " " + mesta[cityChoice])
print("Cena jízdenky je", realPrice)  
print(f"""Děkujeme {firstName} za objednávku,
Vaši jízdenku do města {cityName} za {realPrice} Kč
jsme zaslali na Váš email {mail}. """)
