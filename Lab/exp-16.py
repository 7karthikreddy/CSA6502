print("TEXT EMBEDDINGS AND SEMANTIC SIMILARITY")
print("=" * 45)

documents = [
    "Python is a programming language",
    "Machine learning uses data to make predictions",
    "Artificial Intelligence enables smart machines"
]

query = "What is Python?"

def embedding(text):
    words = text.lower().split()
    return set(words)

def similarity(a, b):
    common = len(a & b)
    total = len(a | b)
    return common / total if total else 0

q = embedding(query)

for doc in documents:
    score = similarity(q, embedding(doc))
    print("\nDocument:", doc)
    print("Similarity:", round(score, 2))
