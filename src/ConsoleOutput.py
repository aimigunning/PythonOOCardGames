from Output import Output

class ConsoleOutput(Output):

    def putOutputValue(self, outputMessage):
        print(outputMessage)