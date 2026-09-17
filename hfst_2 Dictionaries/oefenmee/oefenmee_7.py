# Start de oefen mee met onderstaande dictionary.
gasten = { # Sleutel is naam, waarde is job.
    "Jan":     "reporter",
    "Piet":    "acteur",
    "Joris":   "regisseur",
    "Korneel": "scenarist"
}
namen = ""
while namen :
    gebruiker = input("wie bent u: ")
    if gebruiker in gasten :
        print(f"welkom {gebruiker[namen ]} {gebruiker}.Kom binnen ")
    gasten.pop(namen)