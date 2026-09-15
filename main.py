import pandas as pd

from abstract_calculator import CalculationService
import calculator_v1_0 as c_v1_0
import calculator_v1_1 as c_v1_1
import calculator_v2_0 as c_v2_0
import calculator_v2_1 as c_v2_1
import calculator_v2_2 as c_v2_2
#https://habr.com/ru/articles/1005114/ - хорошая статья


df = pd.read_excel("GoldAndSilver.xlsm", sheet_name="Alg", skiprows=2, usecols="C:I")
df = df.iloc[::-1].reset_index(drop=True)

calculator: CalculationService = c_v2_2.CalculatorV2_2()

calculator.start_buy(df.iloc[0])

for _, row in df.iterrows():
    calculator.buy(row)

last_row = df.iloc[-1]

calculator.print_result(last_row)

#print(df)