from Output import Output

class ConsoleOutput(Output):

    def getOutputValue(self, outputMessage):
        print(outputMessage)