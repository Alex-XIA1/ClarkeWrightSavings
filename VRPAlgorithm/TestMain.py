from Parser import Parser
from StepOneClarkeWright import StepOneClarkeWright

def testParser(filePath):
    parser = Parser()
    data = parser.readFileUsingNumpy(filePath)
    print(data.commandsList)

def testComputeSavings(filePath):
    parser = Parser()
    data = parser.readFileUsingNumpy(filePath)
    clarkWright = StepOneClarkeWright(data)
    print(clarkWright.savingsList)

if __name__ == "__main__":
    filePath = "./instances/instanceTest.txt"
    # testParser(filePath)
    testComputeSavings(filePath)
    