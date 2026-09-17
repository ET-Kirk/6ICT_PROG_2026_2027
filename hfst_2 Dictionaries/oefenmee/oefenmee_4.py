# Gebruik een zelfgemaakte dictionary (of onderstaande).
fruitmand = { # Sleutel is fruit, element is aantal
    "appel": 5,
    "banaan": 3,
    "kers": 50
}
#Niveau1
# gebruiker = input("welk soort fruit zoek je ")
# print(fruitmand[gebruiker])
#Niveau2
gebruiker = input("welk soort fruit zoek je ")
if gebruiker in fruitmand : 
    print(fruitmand[gebruiker])
else:
    print("kan input niet vinden in de fruitmand ")