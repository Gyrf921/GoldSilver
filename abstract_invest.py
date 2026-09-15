from abc import ABC, abstractmethod

class BaseInvest(ABC):

    def __init__(self, start_money=1000):
        self.start_money = start_money

    @abstractmethod
    def invest(self):
        pass

    @abstractmethod
    def print_result(self):
        pass