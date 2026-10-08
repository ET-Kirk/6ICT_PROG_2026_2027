dictionary = {
    "sleutel_1": 4,
    "sleutel_2": 8,
    "sleutel_3": 5,
    "sleutel_4": 0 
}

# Overlopen van een dictionary
print("Dit is de inhoud van de dictionary:")
for sleutel, waarde in dictionary.items():
    print(f" - {sleutel}: {waarde}")
print()

# Wijzigen van ALLE waarden in een dictionary
# (In dit voorbeeld verhogen met 2)
print("Alle waarden in dictionary verhogen met 2")
for sleutel, waarde in dictionary.items():
    dictionary[sleutel] = waarde + 2
print(dictionary)