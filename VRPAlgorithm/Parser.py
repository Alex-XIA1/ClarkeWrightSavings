from Data import Data
from numpy import loadtxt

class Parser:
    def __init__(self):
        pass
    
    # Read the file using loadtxt from numpy
    def readFileUsingNumpy(self, path) -> Data:
        fileElements = loadtxt(path)
        """ In order : number of Demands, number of Vehicles, Capacity of a vehicle and the list 
            of orders """
        numberOfDemands = fileElements[0][0]
        numberOfVehicles = fileElements[0][1]
        vehicleCapacity = fileElements[0][2]
        listOfPositions = []
        for commandNum in range(1,len(fileElements)):
            listOfPositions.append(fileElements[commandNum])
        
        return Data(int(numberOfDemands), int(numberOfVehicles), vehicleCapacity, listOfPositions)