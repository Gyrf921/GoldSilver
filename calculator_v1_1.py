from abstract_calculator import CalculationService


class CalculatorV1_1(CalculationService):

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

        elif -1 <= z_score <= 1:
            return self.BACK_TO_50

        return self.HOLD

    def buy(self, row):
        flag = self.check_zscore(row["Z-score"])

        if flag == self.HOLD:
            return

        if flag == self.BUY_GOLD_75:
            if self.last_operation in (self.BUY_GOLD_75,self.BUY_GOLD_100):
                return

            self.buy_row(row, 0.75, self.BUY_GOLD_100)

        elif flag == self.BUY_GOLD_100:
            if self.last_operation == self.BUY_GOLD_100:
                return

            self.buy_row(row, 1, self.BUY_GOLD_100)

        elif flag == self.BUY_SILVER_75:
            if self.last_operation in (self.BUY_SILVER_75,self.BUY_SILVER_100):
                return

            self.buy_row(row, 0.75, self.BUY_SILVER_100)

        elif flag == self.BUY_SILVER_100:
            if self.last_operation == self.BUY_SILVER_100:
                return

            self.buy_row(row, 1, self.BUY_SILVER_100)

        elif flag == self.BACK_TO_50:
            if self.last_operation == self.BACK_TO_50:
                return

            total_money = (self.count_gold * row["Цена З"] +self.count_silver * row["Цена С"])

            self.count_gold = total_money / 2 / row["Цена З"]
            self.count_silver = total_money / 2 / row["Цена С"]
            self.last_operation = self.BACK_TO_50


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