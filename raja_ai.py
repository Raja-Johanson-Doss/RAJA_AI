from openai import OpenAI

client = OpenAI()

print("🤖 RAJA AI is starting...")
print("Type 'exit' to stop.\n")

conversation = []

while True:
    user_message = input("You: ")

    if user_message.lower() == "exit":
        print("RAJA AI: Goodbye! 👋")
        break

    conversation.append({
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
- Use the previous messages in the conversation to understand context.
- If you are unsure about something, say so instead of making up information.
""",
        input=conversation
    )

    answer = response.output_text

    print("RAJA AI:", answer)

    conversation.append({
        "role": "assistant",
        "content": answer
    })