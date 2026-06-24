import anthropic
from dotenv import load_dotenv
import os

load_dotenv('C:/Users/User/Desktop/.env')
client = anthropic.Anthropic(api_key=os.getenv("ANTHROPIC_API_KEY"))

stocks = [
    {"name": "AAPL", "change": 2.5},
    {"name": "GOOGL", "change": -1.2},
    {"name": "MSFT", "change": 4.1},
    {"name": "TSLA", "change": -3.8},
]

data_text = ""
for stock in stocks:
    data_text += f"{stock['name']}: {stock['change']}%\n"

print("股票数据：")
print(data_text)
print("你可以问我任何关于这些股票的问题（输入'quit'退出）")
print("-" * 40)

while True:
    user_input = input("你的问题：")
    
    if user_input == "quit":
        break
    
    message = client.messages.create(
        model="claude-haiku-4-5",
        max_tokens=1024,
        messages=[
            {"role": "user", "content": f"股票数据：\n{data_text}\n\n用户问题：{user_input}"}
        ]
    )
    
    print("AI：", message.content[0].text)
    print("-" * 40)