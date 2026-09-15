from abstract_calculator import CalculationService


class CalculatorV1_0(CalculationService):

    BUY_GOLD = "BuyGold"
    BUY_SILVER = "BuySilver"

    def check_zscore(self, z_score):
        if z_score > 2:
            return self.BUY_GOLD
        elif z_score < -2:
            return self.BUY_SILVER
        elif -1 <= z_score <= 1:
            return self.BACK_TO_50

        return self.HOLD

    def buy(self, row):
        flag = self.check_zscore(row["Z-score"])

        if flag == self.HOLD:
            return

        if flag == self.BUY_GOLD:

            if self.last_operation == self.BUY_GOLD:
                return

            money = self.count_silver * row["Цена С"]
            self.count_silver = 0

            self.count_gold += money / row["Цена З"]

            self.last_operation = self.BUY_GOLD

        elif flag == self.BUY_SILVER:

            if self.last_operation == self.BUY_SILVER:
                return

            money = self.count_gold * row["Цена З"]
            self.count_gold = 0

            self.count_silver += money / row["Цена С"]

            self.last_operation = self.BUY_SILVER

        elif flag == self.BACK_TO_50:

            if self.last_operation == self.BACK_TO_50:
                return

            total_money = (
                self.count_gold * row["Цена З"] +
                self.count_silver * row["Цена С"]
            )

            self.count_gold = total_money / 2 / row["Цена З"]
            self.count_silver = total_money / 2 / row["Цена С"]

            self.last_operation = self.BACK_TO_50
