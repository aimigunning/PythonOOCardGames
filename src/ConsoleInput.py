from Input import Input

class ConsoleInput(Input):

    def getInputString(self,message):
        return input(message)

    def getInputInteger(self,message):
        return int(input(message))