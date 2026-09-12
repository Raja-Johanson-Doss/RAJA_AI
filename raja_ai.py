from openai import OpenAI
import json
import os

client = OpenAI()

MEMORY_FILE = "memory.json"

# Load saved memory
if os.path.exists(MEMORY_FILE):
    with open(MEMORY_FILE, "r", encoding="utf-8") as file:
        memory = json.load(file)
else:
    memory = []

print("🤖 RAJA AI is starting...")
print("Type 'exit' to stop.\n")

while True:
    user_message = input("You: ")

    if user_message.lower() == "exit":
        print("RAJA AI: Goodbye! 👋")
        break

    memory.append({
        "role": "user",
        "content": user_message
    })

    response = client.responses.create(
        model="gpt-5.6-luna",
        instructions="""
You are RAJA AI, a helpful personal AI assistant.

Your goals:
- Explain things clearly and simply.
- Help with CSE studies and programming.
- Help the user learn Python, C, C++, Java, DSA and other computer science topics.
- Give step-by-step solutions when teaching.
- Be friendly, encouraging and accurate.
- Use previous messages to understand context.
- If you are unsure about something, say so instead of making up information.
""",
        input=memory
    )

    answer = response.output_text

    print("RAJA AI:", answer)

    memory.append({
        "role": "assistant",
        "content": answer
    })

    # Save memory to memory.json
    with open(MEMORY_FILE, "w", encoding="utf-8") as file:
        json.dump(memory, file, indent=4, ensure_ascii=False)