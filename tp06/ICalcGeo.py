from abc import ABC,abstractmethod
# Abstract Base Class


class ICalcGeo(ABC):

    @abstractmethod
    def get_surface(self):
        pass