from sentence_transformers import SentenceTransformer, util

## Load embedding model
model = SentenceTransformer("all-MiniLM-L6-v2")


def plagiarism_score(text):

    # Example reference texts
    references = [
        "Artificial intelligence is transforming healthcare.",
        "AI tools help automate content creation.",
        "Machine learning improves data driven decisions."
    ]

    text_embedding = model.encode(text, convert_to_tensor=True)
    ref_embeddings = model.encode(references, convert_to_tensor=True)

    similarities = util.cos_sim(text_embedding, ref_embeddings)

    max_score = float(similarities.max()) * 100

    return round(max_score, 2) 