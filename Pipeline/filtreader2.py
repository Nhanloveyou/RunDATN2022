from summarize_sbert import summarize_document
from rules_QW import apply_rules
from xlmr_reader import XLMR
import sys
sys.path.insert(0,'./RunDATN2022/Pipeline/')

reader = XLMR(path='./models/XLMR_3')
reader1 = XLMR(path='./models/XLMR_5')
# reader2 = XLMR(path='./models/XLMR_5')
# reader3 = XLMR(path='./models/XLMR_4')
# reader4 = XLMR(path='./models/XLMR_5')

def vireader_predict(context, question, top_k = 5):
  question = apply_rules(question)
  context = summarize_document(context, question, top_k = top_k)
  answer = reader.xlmr_predict(context, question)
  answer1 = reader1.xlmr_predict(context, question)
  # answer2 = reader2.xlmr_predict(context, question)
  # answer3 = reader3.xlmr_predict(context, question)
  # answer4 = reader4.xlmr_predict(context, question)
  list_answer = [answer, answer1]
  return list_answer