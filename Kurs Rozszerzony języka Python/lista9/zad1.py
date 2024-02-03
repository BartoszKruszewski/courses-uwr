import matplotlib.pyplot as plt
import requests

# stare url = 'https://stat.gov.pl/download/gfx/portalinformacyjny/pl/defaultstronaopisowa/4741/1/1/miesieczne_wskazniki_cen_towarow_i_uslug_konsumpcyjnych_od_1982_roku_15-11-2023.csv'
url = 'https://stat.gov.pl/download/gfx/portalinformacyjny/pl/defaultstronaopisowa/4741/1/1/miesieczne_wskazniki_cen_towarow_i_uslug_konsumpcyjnych.csv'

data = list(filter(lambda x: x[0] == 'Rok poprzedni = 100' and x[1] in ('2020', '2021', '2022'), (
    tuple(line.split(';')[2:6])
    for line in requests.get(url).text.split('\n')[:-1]
)))

def get_values(data, year):
    return [
        float(record[3].replace(',', '.')) - 100
        for record in sorted(
            filter(lambda x: x[1] == year, data), key = lambda x: x[2]
        )
    ]

def expected(data1, data2):
    R = 3
    D = 2
    avg1 = sum(data1) / len(data1)
    avg2 = sum(data2) / len(data2)
    diff = avg2 - avg1
    r1, r2 = (1, R - 1) if diff > 0 else (R, R - 1)
    
    return [(d1 * r1 + d2 * r2) / R + diff * D for d1, d2 in zip(data1, data2)]

data2020 = get_values(data, '2020')
data2021 = get_values(data, '2021')
data2022 = get_values(data, '2022')
exp_data2022 = expected(data2020, data2021)

plt.plot(list(range(1, 13)), data2020)
plt.plot(list(range(1, 13)), data2021)
plt.plot(list(range(1, 13)), data2022)
plt.plot(list(range(1, 13)), exp_data2022)
plt.xlabel('Miesiące')
plt.ylabel('Inflacja % (w stosunku do pop. roku)')
plt.legend(['2020', '2021', '2022', '2022 (przewidywana)'])
plt.show()