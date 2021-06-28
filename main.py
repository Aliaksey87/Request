import requests
import json
from datetime import datetime, date, time, timedelta

s1 = 'https://www.nbrb.by/API/ExRates/Rates/Dynamics/145?startDate='
s2 = str(date.today() - timedelta(days=6))           # начальная дата (7 дней назад)
s3 = '&endDate='
s4 = str(date.today())                               # конечная дата (сегодня)
s = (s1 + s2 + s3 + s4)                              # url в сборе
respons = requests.get (
    s
)
data = json.loads(respons.text)
a = []
for x in data:
    a.append(x['Cur_OfficialRate'])
x = round(sum(a)/len(a), 4)
print('Средний курс USD за 7 последних дней:', x, 'BYN')




