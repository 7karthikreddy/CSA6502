from sklearn.metrics.pairwise import cosine_similarity

# Two vectors
vector1 = [[1, 2, 3]]
vector2 = [[2, 4, 6]]

# Cosine Similarity
similarity = cosine_similarity(vector1, vector2)

print("Cosine Similarity:")
print(similarity[0][0])

# Interpretation
if similarity[0][0] > 0.8:
    print("The two vectors are highly similar.")
else:
    print("The two vectors are not highly similar.")
