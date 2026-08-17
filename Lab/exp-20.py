print("DOCUMENT QUESTION ANSWERING USING RAG")
print("=" * 45)

documents = {
    "python": "Python is a high-level programming language.",
    "ai": "Artificial Intelligence enables machines to perform intelligent tasks.",
    "ml": "Machine Learning allows computers to learn from data."
}

question = input("Ask a question: ")

question = question.lower()

if "python" in question:
    context = documents["python"]
elif "artificial intelligence" in question or " ai" in question:
    context = documents["ai"]
elif "machine learning" in question:
    context = documents["ml"]
else:
    context = "No relevant document found."

print("\nRetrieved Context:")
print(context)

print("\nAnswer:")
print(context)
