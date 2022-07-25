from vidr import ViDR
from vireader import vireader_predict
import sys
sys.path.insert(0,'./RunDATN2022/Pipeline/')

path_to_db = './documents/all_documents_viquad.pickle'
ranker = ViDR(path_to_db)

def ViQAS_predict(question):
  retrieve = ranker.ViDR_retriever(question)
  l_answer = []
  for doc in retrieve:
    # print("Đoạn văn:", doc[0], "\n Điểm:", doc[1])
    l_answer.append(vireader_predict(doc[0], question))
  l_score = [(ans[0], 0.75*ans[1]+0.25*doc[1], doc[0]) for ans, doc in zip(l_answer, retrieve)]
  l_score.sort(reverse=True, key=lambda x: x[1])
  top_ans = [(l[0], l[2]) for l in l_score[:5]]
  return top_ans
