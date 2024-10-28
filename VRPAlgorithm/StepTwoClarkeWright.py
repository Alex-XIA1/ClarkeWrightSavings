from StepOneClarkeWright import StepOneClarkeWright
import numpy as np
# Step two of Clarke Wright saving algorithm
class StepTwoClarkeWright:
    def __init__(self, data):
        self.stepOne = StepOneClarkeWright(data)
    
    # Check if we can merge a route
    def checkIfMergeable(self, costOfRoute1, costOfRoute2):
        # Verify that the capacity is enough
        return (costOfRoute1 + costOfRoute2 <= self.stepOne.data.vehicleCapacity)
    
    # Construct a new vehicle route
    def makeNewRoute(self, customerNumber):
        # We will make a route for each customer
        return ([customerNumber], self.stepOne.data.commandsList[customerNumber][0])

    # Insert the new customer
    def mergeRoutes(self, savingIndex, route1, route2):
        # savingsList has elements (node1, node2, savingValue)
        # route has (nodes, cost)
        # we need to know which route will be tail and which one will be head
        node1 = self.stepOne.savingsList[savingIndex][0]
        node2 = self.stepOne.savingsList[savingIndex][1]
        if ((node1 == route1[0][len(route1[0]) - 1] and node2 == route2[0][len(route2[0]) - 1]) or (node1 == route1[0][0] and node2 == route2[0][0])):
            return (route1[0] + list(reversed(route2[0])), route1[1] + route2[1])
        elif (node1 == route1[0][0] and node2 == route2[0][len(route2[0]) - 1]):
            return (route2[0] + route1[0], route1[1] + route2[2])
        elif (node1 == route1[0][len(route1[0]) - 1] and node2 == route2[0][0]):
            return (route1[0] + route2[0], route1[1] + route2[2])
        else :
            return []

    def runAlgorithm(self):
        routeList = []
        # Nothing in the saving, either an error or the instance has issues
        if (len(self.stepOne.savingsList) <= 0) : 
            print("The savings list is empty !")
            return routeList
        # create the routes for all customers
        for customerNumber in range(self.stepOne.data.numberOfCommands - 1):
            routeList.append(self.makeNewRoute(customerNumber + 1))
        print("Initial routeList = ", routeList)
        # go through the savings
        savingsList = self.stepOne.savingsList
        print("Savings list to go through ", savingsList, "\n")
        for savingIndex in range(len(savingsList)):
            # -1 and -2 to simplify a condition lines for the next part, not an issue since we only work by pairs
            indexOfI = -1
            indexOfJ = -2
            # We look for the routes corresponding to i and j, a route has the nodes and its cost
            for routeIndex in range(len(routeList)):
                if (savingsList[savingIndex][0] in routeList[routeIndex][0]):
                    indexOfI = routeIndex
                if (savingsList[savingIndex][1] in routeList[routeIndex][0]):
                    indexOfJ = routeIndex
                # if we found the indexes, we do not explore further
                if (indexOfJ != -2 and indexOfI != -1) :
                    break
            # there is a bug with the code if we go in this 
            if (indexOfI == -1 or indexOfJ == -2):
                print("something is not right with the list of Routes\n")
                return
            # If we have 2 different indexes, then we check the possitibility of merging the routes
            if (indexOfI != indexOfJ):
                route1 = routeList[indexOfI]
                route2 = routeList[indexOfJ]
                if (self.checkIfMergeable(route1[1], route2[1])):
                    # We try to merge the new routes
                    newRoute = self.mergeRoutes(savingIndex, route1, route2)
                    print("The routes ", route1, " and ", route2, " were merged into ", newRoute)
                    # if we successfully merged the routes, we remove the 2 from list and add the new one
                    if (len(newRoute) != 0):
                        toRemove = [indexOfI, indexOfJ]
                        oldRouteList = routeList
                        routeList = [oldRouteList[routeIndex] for routeIndex in range(len(oldRouteList)) if routeIndex not in toRemove]
                        routeList.append(newRoute)
                        print("Route List after merging is ", routeList, "\n")
                        
        return routeList