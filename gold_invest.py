from abstract_invest import BaseInvest


class GoldInvest(BaseInvest):
    FIRST_PRICE = 289.00
    LAST_PRICE = 4398.37
    count_gold = 0

    def invest(self):
        self.count_gold = self.start_money / self.FIRST_PRICE

    def print_result(self):
        result = self.count_gold * self.LAST_PRICE
        print("Итоговая стоимость:", result)
        print("Доходность:", (result / self.start_money - 1) * 100, "%")
        return