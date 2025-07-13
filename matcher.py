import spacy
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

nlp = spacy.load("en_core_web_sm")

def extract_keywords(text):
    """
    Extracts meaningful keywords (nouns, skills, etc.) from given text.
    """
    doc = nlp(text.lower())
    keywords = set()

    for chunk in doc.noun_chunks:
        if len(chunk.text.strip()) > 2:
            keywords.add(chunk.text.strip())

    # Also extract standalone nouns
    for token in doc:
        if token.pos_ in ["NOUN", "PROPN"] and len(token.text) > 2:
            keywords.add(token.text.strip())

    return list(keywords)

def calculate_match_score(resume_text, job_text):
    """
    Uses TF-IDF and cosine[] similarity to measure job-resume relevance.
    """
    documents = [resume_text, job_text]
    tfidf_vectorizer = TfidfVectorizer()
    tfidf_matrix = tfidf_vectorizer.fit_transform(documents)

    score = cosine_similarity(tfidf_matrix[0:1], tfidf_matrix[1:2])[0][0]
    return round(score * 100, 2)  # Percentage match

# Test Example
if __name__ == "__main__":
    resume = """
    Python, Machine Learning, React.js, MySQL, Data Analysis, Model Training, Computer Vision
    """
    job = """
    Looking for a developer with skills in Python, MySQL, Flask, Cloud Deployment, React
    """

    resume_keywords = extract_keywords(resume)
    job_keywords = extract_keywords(job)
    
    print("Resume Keywords:", resume_keywords)
    print("Job Keywords:", job_keywords)

    score = calculate_match_score(" ".join(resume_keywords), " ".join(job_keywords))
    print(f"\nMatch Score: {score}%")