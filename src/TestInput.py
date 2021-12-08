from Input import Input

class TestInput(Input):

    testStringValues = []
    testIntegerValues = []

    def setTestStringValues(self,newTestStringValues):
        for item in newTestStringValues:
            self.testStringValues.append(item)

    def setTestIntegerValues(self,newTestIntegerValues):
        for item in newTestIntegerValues:
            self.testIntegerValues.append(item)

    def getInputString(self,message):
        return self.testStringValues.pop()

    def getInputInteger(self,message):
        return self.testIntegerValues.pop()

