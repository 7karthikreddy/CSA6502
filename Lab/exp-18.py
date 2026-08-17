print("SIMPLE VECTOR DATABASE")
print("=" * 35)

database = []

documents = [
    "Python is easy to learn",
    "Machine learning uses data",
    "AI is used in healthcare",
    "SQL is used for databases"
]

for doc in documents:
    database.append(doc)

query = "Python programming"

print("\nStored Documents:")

for i, doc in enumerate(database):
    print(i + 1, doc)

print("\nQuery:", query)

for doc in database:
    if "python" in doc.lower():
        print("\nRetrieved Document:")
        print(doc)
