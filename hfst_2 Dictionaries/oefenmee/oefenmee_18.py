dambord_2D = [
    ['W', 'Z', 'W', 'Z', 'W', 'Z'],
    ['Z', 'W', 'Z', 'W', 'Z', 'W'],
    ['W', 'Z', 'W', 'Z', 'W', 'Z'],
    ['Z', 'W', 'Z', 'W', 'Z', 'W'],
    ['W', 'Z', 'W', 'Z', 'W', 'Z'],
    ['Z', 'W', 'Z', 'W', 'Z', 'W']]
#Niveau1
rij = int(input("Geef een rij op: "))
kolom= int(input("Geef een kolom op:"))
# print(dambord_2D[rij][kolom])
#Niveau2
if rij % 2 ==0:
    if kolom%2==0:
        print("W")
    else:
        print("Z")
else:
    if kolom%2==0:
        print("Z")
    else:
        print("w")