from vidr import ViDR
from filtreader2 import vireader_predict
import nltk
nltk.download('punkt')

path_to_db = './documents/all_documents_viquad.pickle'
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
    l_answer.append(vireader_predict(doc[0], question))
    i += 1

  l_answer1 = []
  l_answer2 = []
  # l_answer3 = []
  # l_answer4 = []
  # l_answer5 = []
  for i in range(len(l_answer)):
    l_answer1.append(l_answer[i][0])
    l_answer2.append(l_answer[i][1])
    # l_answer3.append(l_answer[i][2])
    # l_answer4.append(l_answer[i][3])
    # l_answer5.append(l_answer[i][4])

  l_score1 = [(ans[0], 0.75*ans[1]+0.25*doc[1], doc[0]) for ans, doc in zip(l_answer1, retrieve)]
  l_score1.sort(reverse=True, key=lambda x: x[1])

  l_score2 = [(ans[0], 0.75*ans[1]+0.25*doc[1], doc[0]) for ans, doc in zip(l_answer2, retrieve)]
  l_score2.sort(reverse=True, key=lambda x: x[1])

  # l_score3 = [(ans[0], 0.75*ans[1]+0.25*doc[1], doc[0]) for ans, doc in zip(l_answer3, retrieve)]
  # l_score3.sort(reverse=True, key=lambda x: x[1])

  # l_score4 = [(ans[0], 0.75*ans[1]+0.25*doc[1], doc[0]) for ans, doc in zip(l_answer4, retrieve)]
  # l_score4.sort(reverse=True, key=lambda x: x[1])

  # l_score5 = [(ans[0], 0.75*ans[1]+0.25*doc[1], doc[0]) for ans, doc in zip(l_answer5, retrieve)]
  # l_score5.sort(reverse=True, key=lambda x: x[1])

  l_score = [l_score1[0][0], l_score2[0][0]]

  return l_score
