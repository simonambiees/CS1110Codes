## this is for checking our tree creation and health ....
from BSTree import BSTree

numbers = []
for value in range(100) :
    numbers.append( (value*value*value - value*2 + 29)%100)

sapling = BSTree()

for thingy in numbers:
    sapling.include(thingy)


print(sapling.showTree())

