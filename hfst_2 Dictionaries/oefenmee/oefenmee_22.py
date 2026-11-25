lijst = [ [4, 5, 1, 9, 3],
          [4, 6, 1],
          [8, 3, 5, 0],
          [7] ]
som = 0
aantal = 0
for rijnummer , sublijst in enumerate(lijst):
    for waarde in sublijst:
        som = som + waarde
        aantal = aantal +1
gem = som /aantal
print(som , gem)
