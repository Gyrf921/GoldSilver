from abstract_calculator import CalculationService


class CalculatorV2_2(CalculationService):

    BUY_GOLD_50 = "BuyGold50"
    BUY_GOLD_100 = "BuyGold100"

    BUY_SILVER_50 = "BuySilver50"
    BUY_SILVER_100 = "BuySilver100"

    def check_zscore(self, z_score):
        if z_score > 10:
            return self.BUY_GOLD_100
        elif z_score >= 5:
            return self.BUY_GOLD_50

        elif z_score < -5:
            return self.BUY_SILVER_100
        elif z_score <= -10:
            return self.BUY_SILVER_50

        return self.HOLD

    def buy(self, row):
        flag = self.check_zscore(row["Z-score"])
        if flag == self.HOLD:
            return

        if flag == self.BUY_GOLD_50:
            if self.last_operation in (self.BUY_GOLD_50,self.BUY_GOLD_100):
                return

            self.buy_row(row, 1, self.BUY_GOLD_50)

        elif flag == self.BUY_GOLD_100:
            if self.last_operation == self.BUY_GOLD_100:
                return

            self.buy_row(row, 1, self.BUY_GOLD_100)

        elif flag == self.BUY_SILVER_50:
            if self.last_operation in (self.BUY_SILVER_50, self.BUY_SILVER_100):
                return

            self.buy_row(row, 0.5, self.BUY_SILVER_50)

        elif flag == self.BUY_SILVER_100:
            if self.last_operation == flag:
                return

            self.buy_row(row, 1, self.BUY_SILVER_100)


    def buy_row(self, row, k_sell, operator):
        if operator in (self.BUY_SILVER_50, self.BUY_SILVER_100):
            gold_to_sell = self.count_gold * k_sell
            money = gold_to_sell * row["Цена З"]

            self.count_gold -= gold_to_sell
            self.count_silver += money / row["Цена С"]
            self.last_price = row["Цена С"]

        elif operator in (self.BUY_GOLD_50, self.BUY_GOLD_100):
            silver_to_sell = self.count_silver * k_sell
            money = silver_to_sell * row["Цена С"]

            self.count_silver -= silver_to_sell
            self.count_gold += money / row["Цена З"]
            self.last_price = row["Цена З"]

        self.last_operation = operator