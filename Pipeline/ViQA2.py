from vidr import ViDR
from pho_predict import phobert_predict
import nltk
nltk.download('punkt')

path_to_db = './RunDATN2022/Pipeline/documents/all_documents_viquad.pickle'
ranker = ViDR(path_to_db)

def ViQAS_predict(question):
  retrieve = ranker.ViDR_retriever(question)
  l_answer = []
  i = 0
  for doc in retrieve:
    # print("Đoạn văn:", doc[0], "\n Điểm:", doc[1])
    # Số lượng

    if len(nltk.word_tokenize(doc[0])) > 400:
      retrieve.pop(i)
      continue
    l_answer.append(phobert_predict(doc[0], question))
    i += 1
  l_score = [(ans[0], 0.75*ans[1]+0.25*doc[1], doc[0]) for ans, doc in zip(l_answer, retrieve)]
  l_score.sort(reverse=True, key=lambda x: x[1])
  return l_score[0][0]