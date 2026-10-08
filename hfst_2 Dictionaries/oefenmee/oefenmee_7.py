# Start de oefen mee met onderstaande dictionary.
gasten = { # Sleutel is naam, waarde is job.
    "Jan":     "reporter",
    "Piet":    "acteur",
    "Joris":   "regisseur",
    "Korneel": "scenarist"
}
namen = ""
while namen == ""  :
    gebruiker = input("wie bent u: ")
    if gebruiker in gasten :
        print(f"welkom {gasten[gebruiker]} {gebruiker} Kom binnen ")
        gasten.pop(gebruiker)
    elif gebruiker == "stop":
        break
    else:
        print(f"de naam {gebruiker} staat niet in de gastenlijst")