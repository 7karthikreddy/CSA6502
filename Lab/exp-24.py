print("DOCUMENT AI ASSISTANT")
print("=" * 35)

document = """
Python is a programming language.
Artificial Intelligence enables intelligent machines.
Machine Learning learns patterns from data.
"""

while True:

    question = input("\nAsk: ")

    if question.lower() == "exit":
        break

    if "python" in question.lower():
        print("Answer: Python is a programming language.")

    elif "artificial intelligence" in question.lower():
        print("Answer: Artificial Intelligence enables intelligent machines.")

    elif "machine learning" in question.lower():
        print("Answer: Machine Learning learns patterns from data.")

    else:
        print("Answer: Information not found in the document.")
