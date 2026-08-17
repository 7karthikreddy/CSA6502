print("MULTI-DOCUMENT AI ASSISTANT")
print("=" * 40)

documents = {

    "AI.txt":
    "Artificial Intelligence enables machines to perform intelligent tasks.",

    "Python.txt":
    "Python is a programming language used in AI and data science.",

    "ML.txt":
    "Machine Learning allows computers to learn from data."
}

print("\nAvailable Documents:")

for name in documents:
    print("-", name)

while True:

    question = input("\nAsk a question: ")

    if question.lower() == "exit":
        print("Assistant: Goodbye!")
        break

    found = False

    for name, content in documents.items():

        if "python" in question.lower() and "Python" in content:
            print("\nDocument:", name)
            print("Answer:", content)
            found = True
            break

        elif "ai" in question.lower() and "Artificial Intelligence" in content:
            print("\nDocument:", name)
            print("Answer:", content)
            found = True
            break

        elif "machine learning" in question.lower() and "Machine Learning" in content:
            print("\nDocument:", name)
            print("Answer:", content)
            found = True
            break

    if not found:
        print("Assistant: No relevant information found.")
