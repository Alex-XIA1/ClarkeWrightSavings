class Data:
    def __init__(self, numberOfDemands, numberOfVehicles, vehicleCapacity, commandsList):
        # number of orders
        self.numberOfCommands = numberOfDemands
        # Number of total vehicle
        self.numberOfVehicles = numberOfVehicles
        # Capacity of a vehicle
        self.vehicleCapacity = vehicleCapacity
        # list containing triples of (cost, xCord, yCord)
        self.commandsList = commandsList