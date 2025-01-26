from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Define your sentences
sentence1 = "I love natural language processing."
sentence2 = "Natural language processing is amazing."

# Create a TF-IDF Vectorizer
vectorizer = TfidfVectorizer()

# Convert sentences to TF-IDF feature vectors
tfidf_matrix = vectorizer.fit_transform([sentence1, sentence2])

# Compute Cosine Similarity
similarity = cosine_similarity(tfidf_matrix[0:1], tfidf_matrix[1:2])

print(f"Sentence Similarity: {similarity[0][0]:.2f}")

# from transformers import AutoTokenizer, AutoModel
# import torch

# # Load a pre-trained model and tokenizer
# model_name = "bert-base-uncased"
# tokenizer = AutoTokenizer.from_pretrained(model_name)
# model = AutoModel.from_pretrained(model_name)

# # Input sentences
# sentence1 = "I love playing football."
# sentence2 = "I enjoy playing soccer."

# # Tokenize and encode sentences
# inputs1 = tokenizer(sentence1, return_tensors="pt", padding=True, truncation=True)
# inputs2 = tokenizer(sentence2, return_tensors="pt", padding=True, truncation=True)

# # Get embeddings from the model
# with torch.no_grad():
#     embedding1 = model(**inputs1).last_hidden_state.mean(dim=1)  # Mean pooling
#     embedding2 = model(**inputs2).last_hidden_state.mean(dim=1)

# # Compute cosine similarity
# cosine_similarity = torch.nn.functional.cosine_similarity(embedding1, embedding2)
# print(f"Sentence similarity: {cosine_similarity.item():.4f}")