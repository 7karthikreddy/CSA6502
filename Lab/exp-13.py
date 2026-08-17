print("LAB 13: API INTEGRATION")
print("=" * 40)

print("Application: AI Question Answering System")

question = input("Enter your question: ")

print("\nSending question to AI API...")
print("Connecting to AI service...")
print("Processing request...")

print("\nAI Response:")

if "python" in question.lower():
    print("Python is a high-level programming language.")
elif "ai" in question.lower():
    print("Artificial Intelligence enables machines to perform")
    print("tasks that normally require human intelligence.")
else:
    print("The AI system generated a response for your question.")

print("\nAPI integration demonstration completed.")
