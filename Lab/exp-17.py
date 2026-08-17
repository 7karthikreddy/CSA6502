import math

print("SEMANTIC SEARCH USING COSINE SIMILARITY")
print("=" * 45)

documents = [
    "python programming language",
    "machine learning algorithms",
    "artificial intelligence",
    "data science and statistics"
]

query = "python programming"

def vector(text):
    words = text.lower().split()
    return words

def cosine(a, b):
    words = list(set(a + b))

    v1 = [a.count(w) for w in words]
    v2 = [b.count(w) for w in words]

    dot = sum(x * y for x, y in zip(v1, v2))

    mag1 = math.sqrt(sum(x*x for x in v1))
    mag2 = math.sqrt(sum(y*y for y in v2))

    if mag1 == 0 or mag2 == 0:
        return 0

    return dot / (mag1 * mag2)

q = vector(query)

results = []

for doc in documents:
    score = cosine(q, vector(doc))
    results.append((score, doc))

results.sort(reverse=True)

print("\nQuery:", query)

print("\nSearch Results:")

for score, doc in results:
    print(round(score, 2), "-", doc)
