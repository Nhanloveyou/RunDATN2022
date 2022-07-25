from underthesea import sent_tokenize
from sentence_transformers import SentenceTransformer, util
import json
import tqdm
from vncorenlp import VnCoreNLP

annotator = VnCoreNLP("./RunDATN2022/Pipeline/VnCoreNLP/VnCoreNLP-1.1.1.jar", annotators="wseg", max_heap_size='-Xmx500m')
model_sbert = SentenceTransformer('./models/model_sbert_phobertlarge_2')

def word_seg(sent):
  return ' '.join([' '.join(s) for s in annotator.tokenize(sent)])

def summarize_document(context, question, top_k=5):
  sentences = sent_tokenize(context)
  if len(sentences) <= top_k:
    return context
  question_embedding = model_sbert.encode(word_seg(question))
  sentences_embedding = [model_sbert.encode(word_seg(sent)) for sent in sentences]
  score_sentences = [(i, float(util.pytorch_cos_sim(question_embedding, sent_embedding)[0][0])) 
                                            for i, sent_embedding in enumerate(sentences_embedding)]
  score_sentences.sort( reverse=True , key=lambda x: x[1])     
  score_sentences = score_sentences[:top_k]
  score_sentences.sort(reverse=False, key=lambda x: x[0]) 

  sentences_new_context = [sentences[i[0]] for i in score_sentences]
  new_context = ' '.join(sentences_new_context)
  return new_context