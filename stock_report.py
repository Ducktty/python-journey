import csv

def classify(price):
    if price > 4:
        return '高'
    else:
        return '低'

prices = []

with open('C:/Users/User/Desktop/stocks.csv') as f:
    reader = csv.reader(f)
    next(reader)
    for row in reader:
        prices.append(float(row[1]))

print('=== 股票分析报告 ===')
print('平均价格:', sum(prices) / len(prices))
print('最高价格:', max(prices))
print('最低价格:', min(prices))
print('')
print('每日分析:')

with open('C:/Users/User/Desktop/stocks.csv') as f:
    reader = csv.reader(f)
    next(reader)
    for row in reader:
        date = row[0]
        price = float(row[1])
        print(date, price, classify(price))