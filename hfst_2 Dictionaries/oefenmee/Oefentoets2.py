""" Oefening 2 (  / 7)
De dictionary 'voorraad' stelt de voorraad van een snackbar voor.
In deze oefening zal je de aantallen en snacks in deze voorraad wijzigen.

Herhaal het volgende tot in het oneindige.
    - Vraag de gebruiker naar een snack.
    - Vraag de gebruiker hoeveel van de snack hij wilt verkopen/aankopen.
        * verkopen = negatief getal || aankopen = positief getal
    - Wijzig de snack in de dictionary voorraad met de opgegeven hoeveelheid.
    - Print hoeveel van deze snack er na de wijziging in de dictionary voorraad zitten.

Het herhalen moet stoppen wanneer de gebruiker 'STOP' invult in plaats van een snack.
Print tenslotte de bekomen dictionary (je mag hiervoor de code uit oef 1 gebruiken).

Hou rekening met volgende drie regels:
    1. Het product bestaat al in de dictionary.
        * Wijzig dan het aantal in de voorraad.
    2. Het product bestaat NIET in de dictionary. 
        * Voeg de snack dan toe als nieuw element samen met de aangekochte hoeveelheid.
    3. Het aantal snacks mag NOOIT kleiner worden dan 0.
        * Print enkel een foutmelding en wijzig niets aan de dictionary voorraad.
"""

""" VOORBEELD 

** REGEL 1: product bestaat al. **
>>> Kies een product: burgers
>>> Hoeveel stuks (negatief = verkoop, positief = aankoop): -5
Er zijn nu 7 burgers in voorraad.

** REGEL 2: product bestaat niet. **
>>> Kies een product: mexicanos
>>> Hoeveel stuks (negatief = verkoop, positief = aankoop): 6
Er zijn nu 6 mexicanos in voorraad.

** REGEL 3: aantal NOOIT kleiner dan 0. **
>>> Kies een product: loempias
>>> Hoeveel stuks (negatief = verkoop, positief = aankoop): -20
Fout! Er zijn slechts 8 loempias in voorraad. Voorraad wordt niet gewijzigd.

** STOPPEN VAN CODE **
>>> Kies een product: STOP
De snackbar heeft volgende snacks op voorraad...
    - burgers: 7
    - loempias: 8
    - frikandellen: 5
    - mexicanos: 6
"""

""" PUNTENVERDELING:
    - Oneindige while-loop + manier om uit te breken: 1
    - Vraag naar user-input + omvormen naar int: 1
    - Wijzig bestaand element in dictionary + conditie: 1.5
    - Maak nieuw bestand aan in dictionary + conditie: 1.5
    - Geef foutmelding als aantal van snack negatief wordt + conditie: 1.5
    - Print boodschap na (eventuele wijziging) + print bekomen dictionary: 0.5

"""
voorraad = {
    "burgers": 12,
    "loempias": 8,
    "frikandellen": 5
}
gebruiker = ""
while gebruiker !="stop":
    gebruiker = input("kies een product: ")
    if gebruiker == "stop":
        break
    aantal_stuks = int(input("hoeveel stuks (negatief = verkoop, positief = aankoop) "))
    if gebruiker in voorraad :
        if aantal_stuks >= 0 :
            voorraad[gebruiker] = voorraad[gebruiker] + aantal_stuks
            print(f"Er zijn nu {voorraad[gebruiker]} {gebruiker} in voorraad.")
        elif aantal_stuks <= 0:
            voorraad[gebruiker] = voorraad[gebruiker] + aantal_stuks
            print(f"Er zijn nu {voorraad[gebruiker]} {gebruiker} in voorraad.")
        else:
            print(f"Fout! Er zijn slechts {voorraad[gebruiker]} {gebruiker} in voorraad. Voorraad wordt niet gewijzigd.")
    else:
        if aantal_stuks >= 0:
            voorraad[gebruiker] = aantal_stuks
            print(f"Er zijn nu {voorraad[gebruiker]} {gebruiker} in voorraad.")
        else:
            print(f"Fout! Er zijn slechts 0 {gebruiker} in voorraad. Voorraad wordt niet gewijzigd.")
print("De snackbar heeft volgende snacks in voorraad:")
for eten,waarde in voorraad.items():
    print(f"- {eten}: {waarde}")
