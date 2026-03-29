from groq import Groq
client = Groq(api_key="groq_api_key")  # updated model

def chat_with_ai(prompt):
    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[
            {"role": "user", "content": prompt}
        ]
    )
    return response.choices[0].message.content


if __name__ == "__main__":
    print("Chatbot is ready! Type 'exit' to quit.\n")
    
    while True:
        user = input("You: ")

        if user.lower() in ["exit", "bye", "quit"]:
            print("Chatbot: Goodbye 👋")
            break

        reply = chat_with_ai(user)
        print("Chatbot:", reply)