""" Oefening 1 (  / 4)
Er is een beveiligingsinbreuk vastgesteld in ons systeem. Uit voorzorg
zal de IT-afdeling de wachtwoorden van een specifieke groep wijzigen. 

Het gaat om alle gebruikers waarvan de gebruikersnaam GEEN punt ('.') bevat.
Pas de wachtwoorden van deze accounts aan. Zet een ! achter hun huidig wachtwoord.
Print op het einde de gewijzigde dictionary, en hoevaak je een wachtwoord hebt gewijzigd.

BELANGRIJK:
De code moet ook werken als de dictionary later uitgebreid wordt.
Doe maar alsof er duizenden gebruikers in de dictionary staan.
"""
gebruikers = {
    'hendrik.clijsters': 'SteDri39',
    'spma300906': 'MauSpi21',
    'bija080714': 'BirJal08',
    'johan.colson': 'ColHan44',
    'momo250308': 'SerRam26'
}


""" VERWACHTE OUTPUT NA OVERLOPEN DICTIONARY:
-------------------------------------------------------------------------------
{'hendrik.clijsters': 'SteDri39', 
 'spma300906': 'MauSpi21!',         --> GEWIJZIGD
 'bija080714': 'BirJal08!',         --> GEWIJZIGD
 'johan.colson': 'ColHan44',        
 'momo250308': 'SerRam26!'          --> GEWIJZIGD
}
Aantal gewijzigde wachtwoorden: 3
-------------------------------------------------------------------------------
"""
teller = 0
for gebr , waarde in gebruikers.items():
    if "." not in gebr :
        waarde = waarde +"!"
        gebruikers[gebr]= waarde
        teller = teller +1
        print(f"{gebr}: {waarde} ,     --> GEWIJZIGD")
    else:
        print(f"{gebr}: {waarde}")
print(f"aantal gewijzigde wachtwoorden zijn {teller}")
