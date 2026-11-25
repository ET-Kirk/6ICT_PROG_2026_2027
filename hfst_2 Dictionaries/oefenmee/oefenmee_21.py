lijst_2D = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
#Niveau1
# for rijnummer , rij in enumerate(lijst_2D):
#     if rijnummer %2 ==0 :
#         for kolomnummer , waarde in enumerate(rij):
#             print(f"{rijnummer} ,{kolomnummer} : {waarde}" )
#Niveau2
for rijnummer , rij in enumerate(lijst_2D):
        for kolomnummer , waarde in enumerate(rij):
            if kolomnummer == rijnummer  :
                    print(f"{rijnummer} ,{kolomnummer} : {waarde}" )
    