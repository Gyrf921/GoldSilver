from abc import ABC, abstractmethod

class CalculationService(ABC):
    BACK_TO_50 = "BackTo50"
    HOLD = "Hold"

    def __init__(self, start_money=1000):
        self.start_money = start_money
        self.last_operation = self.BACK_TO_50

        self.start_gold = 0
        self.start_silver = 0
        self.count_gold = 0
        self.count_silver = 0

    def start_buy(self, row):
        print(row)
        self.count_gold = self.start_money / 2 / row["Цена З"]
        self.start_gold = self.count_gold

        self.count_silver = self.start_money / 2 / row["Цена С"]
        self.start_silver = self.count_silver

    @abstractmethod
    def check_zscore(self, z_score):
        pass

    @abstractmethod
    def buy(self, row):
        pass

    @abstractmethod
    def buy_row(self, row, k_sell, operator):
        pass

    def print_result(self, row):
        print("Золото на начало:", self.start_gold)
        print("Золото:", self.count_gold)
        print("Серебро на начало:", self.start_silver)
        print("Серебро:", self.count_silver)
        result = (
                self.count_gold * row["Цена З"] +
                self.count_silver * row["Цена С"]
        )
        print("Итоговая стоимость:", result)
        print("Доходность:", (result / self.start_money - 1) * 100, "%")
        return