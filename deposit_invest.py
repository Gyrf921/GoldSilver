from abstract_invest import BaseInvest

class DepositInvest(BaseInvest):

    PERCENT = 10
    start_money = 0
    money = 0

    def invest(self):
        self.money = self.start_money
        for i in range(26):
            self.money *= 1 + self.PERCENT / 100

    def print_result(self):
        print("Итоговая сумма на счёте:", self.money)
        print("Доходность:", (self.money / self.start_money - 1) * 100, "%")
        return