import anthropic
import csv
from dotenv import load_dotenv
import os

load_dotenv('C:/Users/User/Desktop/.env')

client = anthropic.Anthropic(api_key=os.getenv("ANTHROPIC_API_KEY"))

prices = []
with open('C:/Users/User/Desktop/stocks.csv') as f:
    reader = csv.reader(f)
    next(reader)
    for row in reader:
        prices.append(float(row[1]))

average = sum(prices) / len(prices)
highest = max(prices)
lowest = min(prices)

prompt = f"""以下是一组股票价格数据：
平均价格：{average:.2f}
最高价格：{highest}
最低价格：{lowest}
所有价格：{prices}

请用两句话给出简短的分析。"""

message = client.messages.create(
    model="claude-sonnet-4-6",
    max_tokens=1024,
    messages=[
        {"role": "user", "content": prompt}
    ]
)

print(message.content[0].text)