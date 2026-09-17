# Start de oefen mee met onderstaande dictionary.
fruitmand = { # Sleutel is fruit, waarde is aantal
    "appel": 5,
    "banaan": 3,
    "kers": 50
}
#niveau1
# Print de dictionary-waarde gekoppeld aan onderstaande variabele
# fruit = "banaan"
# print( fruitmand[fruit] )
#Niveau2
# nieuw_fruit  = "mango"
# nieuw_aantal = 1
# fruitmand[nieuw_fruit] = nieuw_aantal
# print(fruitmand)
#Nivuea3
# fruit = "banaan"
# nieuw_aantal = 8
# fruitmand[fruit] = nieuw_aantal
# print(fruitmand)
#Niveua4
# fruit = "kers"
# fruitmand["kers"] -= 43
# print(fruitmand)
#Niveau5
terugleggen_fruit = "kers"
fruitmand.pop(terugleggen_fruit)
print(fruitmand)