
## Команды для локального запуска:

``` Установка локального окружения
python -m venv .venv 
```

``` Установка необходимых библиотек
pip install openpyxl
pip install pandas 
``` 

## Метод работы
Для смены вариантов калькулятора найдите 15 строку файла main.py

``` Нужная строка
calculator: CalculationService = c_v2_2.CalculatorV2_2()
``` 


Меняя в ней присвоение c_v2_2.CalculatorV2_2(), можно выбрать любую нужную версию

В примере указана версия 2.2, соотвественно всё ссылается на модуль [calculator_v2_2.py](calculator_v2_2.py) и единственный внутренний класс

Для примера поменяем версию на 1.1, смотрим импорты главного файла

``` Импорты
import calculator_v1_0 as c_v1_0
import calculator_v1_1 as c_v1_1
import calculator_v2_0 as c_v2_0
import calculator_v2_1 as c_v2_1
import calculator_v2_2 as c_v2_2
```

Тут выбираем нужную нам версию c_v1_1 и обращаемся к ней вместе c_v2_2

```Пример
calculator: CalculationService = c_v1_1.CalculatorV1_1()
```

Теперь при запуске для расчёта будет использоваться версия v1.1 
