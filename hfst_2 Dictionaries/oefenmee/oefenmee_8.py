# Start de oefen mee met onderstaande dictionary.
steden_temp = { # Sleutel is stad, waarde is temp 
    "Hasselt": 25,
    "Oostende": 21,
    "Antwerpen": 24,
    "Brussel": 23,
    "Luik": 23,
    "Namen": 24
}
gebruiker = input("welke stad bent u : ")
if gebruiker in steden_temp:
    print(f"het is hier {steden_temp.get(gebruiker)} °C")
else:
    print("Het is hier ??? °C")
