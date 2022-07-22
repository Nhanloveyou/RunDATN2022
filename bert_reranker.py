from sentence_transformers import CrossEncoder

model = CrossEncoder('amberoad/bert-multilingual-passage-reranking-msmarco', max_length=512)

def bert_rerank(question, docs, top_rerank=10):
  input = [(question, doc) for doc in docs]
  scores = list(model.predict(input))
  scores=[(i, s) for i, s in enumerate(scores)]
  scores = [(docs[j[0]], j[1][1]) for j in scores]
  scores.sort(reverse=True, key=lambda x: x[1])
  rank = [i for i in scores[:top_rerank]]
  return rank