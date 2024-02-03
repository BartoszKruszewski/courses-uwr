from datetime import datetime, timedelta
from model import Model
import matplotlib.pyplot as pt

START_DATE = '04.03.2020'

def normalize(date):
    start_date = datetime.strptime(START_DATE, '%d.%m.%Y')
    given_date = datetime.strptime(date, '%d.%m.%Y')
    delta = given_date - start_date
    return delta.days

def get_date(normalized_date):
    start_date = datetime.strptime(START_DATE, '%d.%m.%Y')
    result_date = start_date + timedelta(days=normalized_date)
    return result_date.strftime('%d.%m.%Y')

with open('dane_covid_ilosc_przypadkow.csv', 'r') as file:
    data = [
        (normalize(p[0]), int(p[1]))
        for p in [
            line.rstrip().split(';')
            for line in file.readlines()
        ]
    ]

model = Model(data, train_mode = 'data', data_split_ratio = 0.1)
# model = Model(data, train_mode = 'e', max_n = 15)
print(f'Best n: {model.best_n}')
print(f'E train for best n: {(model.best_e * 100):.2f}%')
print(f'E global for best n: {(model.e(model.best_n) * 100):.2f}%')

# ostatnie dane: 12.03.2022 - 5799504 przypadkow
PREDICTIONS = [
    '13.03.2022',
    '15.03.2022',
    '20.03.2022',
    '20.04.2022',
    '20.05.2022',
    '20.06.2022',
    '28.07.2022',
    '24.10.2022'
]

for prediction in PREDICTIONS:
    print(f'Date: {prediction}: {model(normalize(prediction))}')

pt.plot([p[0] for p in data], [p[1] for p in data], label='Real Data')
pt.plot(list(range(800)), [model(i) for i in range(800)], label='Aproxymation')
pt.legend()
pt.show()


