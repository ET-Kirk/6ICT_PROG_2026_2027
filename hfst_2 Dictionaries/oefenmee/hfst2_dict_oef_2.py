""" Oefening 2 (  / 6)
Het kassasysteem van een bistro houdt de openstaande rekeningen per tafel bij.
In deze oefening ga je bestellingen toevoegen of tafels laten afrekenen.

Herhaal het volgende tot de gebruiker 'STOP' ingeeft bij de tafelnaam:
    - Vraag naar de tafelnaam (bv. 'Tafel 1').
    - Vraag welke actie de kelner wil uitvoeren: 'bestellen' of 'afrekenen'.

bestellen:
    - Vraag naar het bedrag van de nieuwe bestelling.
    - Als de tafel AL bestaat: tel het bedrag op bij de huidige rekening.
    - Als de tafel NOG NIET bestaat: voeg de tafel toe met dit bedrag.
    - Print de nieuwe totale rekening voor deze tafel.

afrekenen:        
    - Als de tafel AL bestaat: verwijder de tafel uit de dictionary met .pop()
      en print het totaal afgerekende bedrag.
    - Als de tafel NOG NIET bestaat: print een foutmelding dat er geen 
      openstaande rekening is voor deze tafel.

Print na het stoppen van de loop een overzicht van alle nog openstaande tafels.
"""

tafels = {
    'Tafel 1': 45.50,
    'Tafel 3': 22.00,
    'Tafel 4': 87.10
}


""" VOORBEELD:
-------------------------------------------------------------------------------
Voer tafelnaam in: Tafel 1
Welke actie ('bestellen' of 'afrekenen')? bestellen
Voer het bedrag in: 12.50
Nieuw totaal voor Tafel 1: €58.0

Voer tafelnaam in: Tafel 3
Welke actie ('bestellen' of 'afrekenen')? afrekenen
Tafel 3 heeft €22.0 afgerekend en is nu vrij.

Voer tafelnaam in: Tafel 2
Welke actie ('bestellen' of 'afrekenen')? afrekenen
Fout: Tafel 2 heeft geen openstaande rekening!

Voer tafelnaam in: STOP

Nog openstaande rekeningen:
{'Tafel 1': 58.0, 'Tafel 4': 87.1}
-------------------------------------------------------------------------------
"""

# gebruiker = ""
# while gebruiker !="stop":
#     gebruiker = input("voer tafelnaam in : ")
#     if gebruiker == "stop":
#         break
#     welk_actie = input("Welke actie ('bestellen' of 'afrekenen')?")
#     if welk_actie == "bestellen" :
#         bestelling = int(input("Voer het bedrag in:"))
#         tafels[gebruiker]  =  tafels[gebruiker] + bestelling
#         print(f"Nieuw totaal voor {gebruiker} is {tafels[gebruiker]} euro")
#     else:
#         if welk_actie == "afrekenen":
#            if tafels[gebruiker] > 0:
#                 tafels[gebruiker] = 0 
#                 print(f"{gebruiker} heeft {tafels[gebruiker]} afgerekend en is nu vrij")
#         else :
#             if tafels[gebruiker] == 0 :
#                 print(f"Fout: {tafels[gebruiker]} heeft geen openstaande rekening!")
# print("Nog openstaande rekeningen:")
# for tafelnummer,bedrag in tafels.items():
#     print(f"- {tafelnummer}: {bedrag}")


while True :
    tafelnaam = input("geef tafelnaam op")
    actie =  input("bestellen of afrekenen")
    if tafelnaam == "stop":
        break
    if actie == "bestellen":
        bedrag = float(input("hoeveel bijrekenen"))
        if tafelnaam in tafels:
            tafels[tafelnaam] =tafels[tafelnaam]  + bedrag
        else:
            tafels[tafelnaam] = bedrag

    elif actie == "afrekenen":
        if tafelnaam in tafels:
            print(f"ze zijn {tafels[tafelnaam]} euro schuldig")
            tafels.pop(tafelnaam)
        else:
            print(f"fout. Tafel bestaat niet ")