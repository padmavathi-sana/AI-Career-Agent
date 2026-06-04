from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

model = SentenceTransformer('all-MiniLM-L6-v2')

def resume_job_score(resume, job):
    emb = model.encode([resume, job])
    return round(cosine_similarity([emb[0]], [emb[1]])[0][0] * 100, 2)