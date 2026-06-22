# 我的第一个数据分析程序
stocks = [2.5, 4.1, 1.8, 6.3, 3.9, 2.2, 5.7]

average = sum(stocks) / len(stocks)
highest = max(stocks)
lowest = min(stocks)

print('平均值:', average)
print('最高:', highest)
print('最低:', lowest)

if average > 4:
    print('表现良好')
else:
    print('表现一般')
