""" OEFENING 3 (  / 5)
Onderstaande datastructuur bevat als elementen de vragen/antwoorden van een quiz-spel.
Hiernaast bevat het ook hoeveel geld iedere vraag waard is.
Sommige vragen hebben ook een hint. Die hint mag enkel getoond worden als ze aanwezig is.

Stel iedere vraag aan de deelnemer (via de functie input).
Toon eerst de hint als deze bestaat (ZIE VOORBEELD).

Controleer het antwoord en print of de deelnemer het juist/fout had.
 - Heeft de deelnemer het juist? Voeg het gewonnen geld dan toe aan een prijzenpot.
 - Heeft de deelnemer het fout? Print dan ook wat het juiste antwoord was.
Na het overlopen van alle elementen print je hoeveel geld de deelnemer gewonnen heeft.

De code moet blijven werken, ook als er later vragen bijkomen of weggaan.
"""

""" VOORBEELD:
Hint: Tussen 3 en 5
Wat is 2+2? 4
Correct! Je verdient €200.

Hint: denk aan 'for' en 'while'
Hoe kan je code meermaals herhalen? if
Fout! Het juiste antwoord is loops

Welk datatype stelt een kommagetal voor? float
Correct! Je verdient €400.

De quiz is afgelopen. Je hebt €600 gewonnen!4
"""
prijs_pot = 0
quiz = [
    {"vraag":"Wat is 2+2?", "antwoord":"4", "geld":200, "hint":"Tussen 3 en 5"},
    {"vraag":"Hoe kan je code meermaals herhalen?", "antwoord":"loops", "geld":300, "hint":"Denk aan 'for' en 'while'"},
    {"vraag":"Welk datatype stelt een kommagetal voor?", "antwoord":"float", "geld":400},
]
for index, waarde in enumerate(quiz):
    if "hint" in waarde:
        print(f"hint: {waarde["hint"]}")
        gebr = input(f"{waarde["vraag"]}: ")
        if gebr == waarde["antwoord"]:
            prijs_pot = prijs_pot + waarde["geld"]
            print(f"correct! Je verdient {prijs_pot} euro")
        else:
            print(f"fout! het juiste antwoord is {waarde["antwoord"]}")
    else:
        gebr = input(f"{waarde["vraag"]}: ")
        if gebr == waarde["antwoord"]:
            prijs_pot = prijs_pot + waarde["geld"]
            print(f"correct! Je verdient {prijs_pot} euro")
        else:
            print(f"fout! het juiste antwoord is {waarde["antwoord"]}")
print(f"de quiz is afgelopen. Je hebt {prijs_pot} euro gewonnen!")
