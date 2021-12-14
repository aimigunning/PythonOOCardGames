from abc import abstractmethod, ABC

class Output(ABC):
    @abstractmethod
    def putOutputValue(self, outputMessage):
        pass