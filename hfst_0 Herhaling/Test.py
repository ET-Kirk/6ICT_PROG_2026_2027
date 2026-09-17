#Versie 1
nummers = ["+32 470 998301" , "+32 483 313220" , "+32 453 231 456"]

namen = ["jan","Piet","kapper korneel"]

# gebruiker = input("wat is je naam: ")
# if gebruiker in namen :
#     if gebruiker == "jan":
#         print("jan ,+32 470 998301")
#     elif gebruiker == "Piet":
#         print("Piet ,+32 483 313220 ")
#     else :
#         print("Kapper Korneel ,+32 453 231 456")
# else:
#     print("naam komt niet voor ")


#Versie 2
# naam_gebr = input("geef me je naam:")
# for index , naam in enumerate(namen):
#     if naam_gebr == naam : 
#         print(nummers[index])


telefoonboek = {"jan":"+32 470 998301",
                "Piet": "+32 483 313220" , 
                "Kapper Korneel":"+32 453 231 456" }

naam_gebr = input("geef mij de naam ")
if naam_gebr in telefoonboek:
    print(telefoonboek[naam_gebr])
else:
    print("naam bestaat niet ")