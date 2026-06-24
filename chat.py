import anthropic
from dotenv import load_dotenv
import os

load_dotenv('C:/Users/User/Desktop/.env')
client = anthropic.Anthropic(api_key=os.getenv("ANTHROPIC_API_KEY"))

conversation = []

print("开始对话（输入 quit 退出）")

while True:
    user_input = input("你：")
    
    if user_input == "quit":
        break
    
    conversation.append({
        "role": "user",
        "content": user_input
    })
    
    message = client.messages.create(
        model="claude-sonnet-4-6",
        max_tokens=1024,
        messages=conversation
    )
    
    reply = message.content[0].text
    print("AI：", reply)
    
    conversation.append({
        "role": "assistant",
        "content": reply
    })