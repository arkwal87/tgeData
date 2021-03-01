from datetime import datetime, timedelta

holidays = [
    "01-01-2021",
    "06-01-2021",
    "05-04-2021",
    "06-04-2021",
    "01-05-2021",
    "03-05-2021",
    "03-06-2021",
    "15-08-2021",
    "01-11-2021",
    "11-11-2021",
    "25-12-2021",
    "26-12-2021"
]


def myFunc(singleDate):
    test2 = datetime.strptime(singleDate, '%d-%m-%Y').date()
    return test2


hol = list(map(lambda test: datetime.strptime(test, '%d-%m-%Y').date().strftime('%d-%m-%Y'), holidays))

hol2 = [datetime.strptime(i, '%d-%m-%Y').date().strftime('%d-%m-%Y') for i in holidays]

print(hol2[0])
print(list(hol2))

print("26-12-2021" in hol2)

print(hol)