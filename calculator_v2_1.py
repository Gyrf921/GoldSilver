from abstract_calculator import CalculationService


class CalculatorV2_1(CalculationService):

    BUY_GOLD_75 = "BuyGold75"
    BUY_GOLD_100 = "BuyGold100"

    BUY_SILVER_75 = "BuySilver75"
    BUY_SILVER_100 = "BuySilver100"

    def check_zscore(self, z_score):
        if z_score > 4:
            return self.BUY_GOLD_100
        elif z_score >= 2:
            return self.BUY_GOLD_75

        elif z_score < -4:
            return self.BUY_SILVER_100
        elif z_score <= -2:
            return self.BUY_SILVER_75

        return self.HOLD

    def buy(self, row):
        flag = self.check_zscore(row["Z-score"])

        if flag == self.HOLD:
            return

        if flag == self.BUY_GOLD_75:

            if self.last_operation in (
                self.BUY_GOLD_75,
                self.BUY_GOLD_100
            ):
                return

            self.buy_row(row, 0.75, self.BUY_GOLD_100)

        elif flag == self.BUY_GOLD_100:

            if self.last_operation == self.BUY_GOLD_100:
                return

            self.buy_row(row, 1, self.BUY_GOLD_100)

        elif flag == self.BUY_SILVER_75:

            if self.last_operation in (
                self.BUY_SILVER_75,
                self.BUY_SILVER_100
            ):
                return

            self.buy_row(row, 0.75, self.BUY_SILVER_100)

        elif flag == self.BUY_SILVER_100:

            if self.last_operation == self.BUY_SILVER_100:
                return

            self.buy_row(row, 1, self.BUY_SILVER_100)

    def buy_row(self, row, k_sell, operator):
        if operator in (self.BUY_SILVER_75, self.BUY_SILVER_100):
            silver_to_sell = self.count_silver * k_sell
            money = silver_to_sell * row["Цена С"]

            self.count_silver -= silver_to_sell
            self.count_gold += money / row["Цена З"]

        elif operator in (self.BUY_GOLD_75, self.BUY_GOLD_100):
            silver_to_sell = self.count_silver * k_sell
            money = silver_to_sell * row["Цена С"]

            self.count_silver -= silver_to_sell
            self.count_gold += money / row["Цена З"]

        self.last_operation = operator