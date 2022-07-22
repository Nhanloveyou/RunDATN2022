from drqa import retriever
import json
import tqdm
import pickle

ranker = retriever.get_class('tfidf')(tfidf_path='./all_documents_viquad-tfidf-ngram=2-hash=16777216-tokenizer=simple.npz')

with open('./documents/all_documents_viquad.pickle', 'rb') as f:
  all_docs = pickle.load(f)

def tfidf_drqa(query, k=5109):
  doc_names, doc_scores = ranker.closest_docs(query, k)
  return doc_names, doc_scores

def retriever(question, top_k = 5109):
  doc_names, doc_scores = tfidf_drqa(question)
  result = [(list(all_docs.keys())[int(idx)], score) for idx, score in zip(doc_names, doc_scores)]
  return result[:top_k]