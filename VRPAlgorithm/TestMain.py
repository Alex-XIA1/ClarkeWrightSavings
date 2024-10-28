from Parser import Parser
from StepOneClarkeWright import StepOneClarkeWright
from StepTwoClarkeWright import StepTwoClarkeWright

def testParser(filePath):
    parser = Parser()
    data = parser.readFileUsingNumpy(filePath)
    print(data.commandsList)

def testComputeSavings(filePath):
    parser = Parser()
    data = parser.readFileUsingNumpy(filePath)
    clarkWright = StepOneClarkeWright(data)
    print(clarkWright.savingsList)

def testMergeable(filePath):
    parser = Parser()
    data = parser.readFileUsingNumpy(filePath)
    clarkWrightAll = StepTwoClarkeWright(data)
    print(clarkWrightAll.checkIfMergeable(4,7))
    print(clarkWrightAll.checkIfMergeable(2,4))

def testCreateRoute(filePath):
    parser = Parser()
    data = parser.readFileUsingNumpy(filePath)
    clarkWrightAll = StepTwoClarkeWright(data)
    print(clarkWrightAll.makeNewRoute(1))

def testAlgorithm(filePath):
    parser = Parser()
    data = parser.readFileUsingNumpy(filePath)
    clarkWrightAll = StepTwoClarkeWright(data)
    clarkWrightAll.runAlgorithm()

if __name__ == "__main__":
    filePath = "./instances/instanceTest.txt"
    # testParser(filePath)
    # testComputeSavings(filePath)
    # testMergeable(filePath)
    # testCreateRoute(filePath)
    testAlgorithm(filePath)
    