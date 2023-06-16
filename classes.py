
class parts:
    def __init__(self, partNumber, partName):
        self.partNumber = partNumber 
        self.partName = partName

partsList = []
screw = parts(5, 'screw')
partsList.append(screw)
screwDriver = parts(6, 'screw driver')
partsList.append(screwDriver)
partsList.append(parts(7, 'hammer'))
for i in range(len(partsList)):
    print('The part number is: ' + str(partsList[i].partNumber) + ', the name of this part is: ' + partsList[i].partName)