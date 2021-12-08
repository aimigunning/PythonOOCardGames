from abc import abstractmethod, ABC


class Input(ABC):
    @abstractmethod
    def getInputString(self,message):
        pass

    @abstractmethod
    def getInputInteger(self,message):
        pass