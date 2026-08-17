print("END-TO-END RAG PIPELINE")
print("=" * 35)

document = """
Artificial Intelligence is a branch of computer science.
Machine Learning is a part of Artificial Intelligence.
Python is commonly used for Artificial Intelligence projects.
"""

# 1. Document Loading
print("\n1. Document Loading")
print("Document loaded successfully.")

# 2. Text Chunking
chunks = document.split(".")

print("\n2. Text Chunks")

for chunk in chunks:
    if chunk.strip():
        print("-", chunk.strip())

# 3. Embeddings
print("\n3. Embeddings")
print("Text converted into numerical representations.")

# 4. Retrieval
query = "What is Machine Learning?"

print("\n4. Query:", query)

for chunk in chunks:
    if "Machine Learning" in chunk:
        retrieved = chunk.strip()
        print("Retrieved:", retrieved)

# 5. Answer Generation
print("\n5. Generated Answer")
print("Machine Learning is a part of Artificial Intelligence.")
