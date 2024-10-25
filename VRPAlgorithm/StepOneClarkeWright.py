import numpy as np

# Step one of clarke Wright, compute all the savings with this class
class StepOneClarkeWright:
    def __init__(self, data):
        self.data = data
        # distances of size number of points * number of points
        self.distancesMatrix = self.calculateDistances(self.data)
        # savings of size number of points * number of points with 0 for warehouse
        self.savingsList = self.computeSavings(self.distancesMatrix)

    def calculateDistances(self, data):
        # We initiate a distance Matrix with all values 0
        positions = data.commandsList
        distancesMatrix = np.zeros((len(positions), len(positions)))
        for distancesIndexI in range(distancesMatrix.shape[0]):
            for distancesIndexJ in range(distancesMatrix.shape[1]):
                # We ignore the cost in distance calculations
                iPosition = positions[distancesIndexI][1:]
                jPosition = positions[distancesIndexJ][1:]
                distancesMatrix[distancesIndexI, distancesIndexJ] = self.calculateOneDistance(iPosition, jPosition)
        return distancesMatrix

    # Compute all the savings using ClarkeWright formula
    def computeSavings(self, distancesMatrix):
        savingsList = []
        # Warehouse is not counted in the savings calculation
        for demandNumberI in range(1, len(distancesMatrix)):
            for demandNumberJ in range(demandNumberI, len(distancesMatrix)):
                distanceIJ = distancesMatrix[demandNumberI, demandNumberJ]
                distanceIToWarehouse = distancesMatrix[demandNumberI, 0]
                distanceWarehouseToJ = distancesMatrix[0, demandNumberJ]
                savingValue = self.clarkeWrightSaving(distanceWarehouseToJ, distanceIToWarehouse, distanceIJ)
                savingsList.append((demandNumberI, demandNumberJ, savingValue))
        # We order the savings from best to lowest 
        savingsList.sort(key = lambda triple : triple[2], reverse=True)
        return savingsList

    # calculate saving for 2 positions i and j : ci0 + c0j - cij
    def clarkeWrightSaving(self, distanceWarehousetoJ, distanceIToWarehouse, distanceIJ):
        return distanceIToWarehouse + distanceWarehousetoJ - distanceIJ

    # calculate the distance between position i and j
    def calculateOneDistance(self, iPosition, jPosition):
        return np.linalg.norm(iPosition - jPosition)