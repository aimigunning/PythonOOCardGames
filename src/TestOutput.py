from Output import Output

class TestOutput(Output):
    testOutputValues = []

    def putOutputValue(self, outputMessage):
        self.testOutputValues.append(outputMessage)

    def getTestOutputValues(self):
        return self.testOutputValues