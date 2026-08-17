print("TOP-K DOCUMENT RETRIEVAL")
print("=" * 35)

documents = [
    "Python is a programming language",
    "Python is used in data science",
    "Machine learning uses algorithms",
    "AI is used in healthcare",
    "Python is useful for automation"
]

query = "Python"

scores = []

for doc in documents:

    if "python" in doc.lower():
        score = 1
    else:
        score = 0

    scores.append((score, doc))

scores.sort(reverse=True)

k = 3

print("\nTop", k, "Documents:")

for score, doc in scores[:k]:
    print("-", doc)
