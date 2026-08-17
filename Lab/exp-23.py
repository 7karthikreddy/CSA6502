print("CONTEXT-AWARE CHATBOT")
print("=" * 35)

context = []

while True:

    question = input("\nYou: ")

    if question.lower() == "exit":
        print("Bot: Goodbye!")
        break

    context.append(question)

    if "python" in question.lower():
        answer = "Python is a programming language."

    elif "use" in question.lower() and len(context) > 1:
        answer = "Python is widely used in AI, data science and automation."

    else:
        answer = "Please ask a question related to Python."

    print("Bot:", answer)

    print("Context:", context)
