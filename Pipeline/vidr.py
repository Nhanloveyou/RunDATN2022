from ViDR_ranker import retriever
from summarize_sbert import summarize_document
from bert_reranker import bert_rerank
from rules_QW import apply_rules
import pickle

class ViDR():
  def __init__(self, path='./RunDATN2022/Pipeline/documents/all_documents_viquad.pickle'):
    with open(path, 'rb') as f:
      self.all_docs = pickle.load(f)

  def ViDR_retriever(self, question, top_k=10):
    # apply rules
    question = apply_rules(question)
    # ranker
    result = retriever(question, top_k=100)
    l_docs = [self.all_docs[k[0]] for k in result]
    # summarize
    l_docs = [summarize_document(doc, question, top_k=5) for doc in l_docs]
    # re-ranker
    l_docs = bert_rerank(question, l_docs)
    return l_docs