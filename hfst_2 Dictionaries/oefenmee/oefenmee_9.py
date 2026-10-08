# Start de oefen mee met onderstaande dictionary.
recept = { # Sleutel is ingredi?nt, waarde is hoeveelheid
    "Aardappelen": 800,
    "Wortelen": 500,
    "erwten": 300,
    "Worsten": 400
}
gebruiker = int(input("voor hoeveel man kook je :"))
for voedsel,waarde in recept.items():
    waarde = waarde //4 * gebruiker
    print(f"- {voedsel} : {waarde} gr" )





