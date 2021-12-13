from Output import Output

class TestOutput(Output):
    testOutputValues = []

    def setOutputValue(self, outputMessage):
        for item in outputMessage:
            self.testOutputValues.append(item)

    def getOutputValue(self, outputMessage):
        return self.testOutputValues.pop()