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
    l_answer.append(vireader_predict(doc[0], question))
  l_score = [(ans[0], 0.75*ans[1]+0.25+doc[1]) for ans, doc in zip(l_answer, retrieve)]
  l_score.sort(reverse=True, key=lambda x: x[1])
  return l_score[0][0]
