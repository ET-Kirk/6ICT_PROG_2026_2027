from random import randint

lijst_2D = [ [randint(0,5), randint(0,5), randint(0,5)],
             [randint(0,5), randint(0,5), randint(0,5)],
             [randint(0,5), randint(0,5), randint(0,5)] ]
#Niveau1
# lijst_2D[0][1] = randint(0,6)
# lijst_2D[2][0] = randint(0,6)
# print(lijst_2D[0][1] ,lijst_2D[2][0]  )
#Niveau2
lijst_2D[1][1] = randint(0,5) *-1
lijst_2D[2][2] = randint(0,5) *-1
print(lijst_2D[1][1] ,lijst_2D[2][2] )
