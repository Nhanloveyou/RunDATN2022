from summarize_sbert import summarize_document
from rules_QW import apply_rules
from xlmr_reader import XLMR

reader = XLMR(path='./RunDATN2022/Pipeline/models/vireaderplusBiLSTMAdd4-finetuned-viquad')

def vireader_predict(context, question, top_k = 5):
  question = apply_rules(question)
  context = summarize_document(context, question, top_k = top_k)
  answer = reader.xlmr_predict(context, question)
  return answer