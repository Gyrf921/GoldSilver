import pandas as pd

from abstract_calculator import CalculationService
import calculator_v1_0 as c_v1_0
import calculator_v1_1 as c_v1_1
import calculator_v2_0 as c_v2_0
import calculator_v2_1 as c_v2_1
import calculator_v2_2 as c_v2_2
from abstract_invest import BaseInvest
import deposit_invest as deposit_i
import gold_invest as gold_i


#https://habr.com/ru/articles/1005114/ - хорошая статья

def calc_gold_and_silver():
    df = pd.read_excel("GoldAndSilver.xlsm", sheet_name="Alg", skiprows=2, usecols="C:I")
    df = df.iloc[::-1].reset_index(drop=True)

    calculator: CalculationService = c_v2_2.CalculatorV2_2()

    calculator.start_buy(df.iloc[0])

    for _, row in df.iterrows():
        calculator.buy(row)

    last_row = df.iloc[-1]

    calculator.print_result(last_row)


def calc_gold_invest():
    invest: BaseInvest = gold_i.GoldInvest()
    invest.invest()
    invest.print_result()

def calc_deposit_invest():
    invest: BaseInvest = deposit_i.DepositInvest()
    invest.invest()
    invest.print_result()


calc_gold_and_silver()
