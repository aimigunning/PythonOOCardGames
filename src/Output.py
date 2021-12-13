from abc import abstractmethod, ABC

class Output(ABC):
    @abstractmethod
    def getOutputValue(self, outputMessage):
        pass