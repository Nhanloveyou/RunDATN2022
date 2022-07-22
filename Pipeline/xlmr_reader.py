from transformers import AutoModelForQuestionAnswering, AutoTokenizer
import numpy as np

class XLMR():
  def __init__(self, path='./models/vireaderplusBiLSTMAdd4-finetuned-viquad'):
    self.tokenizer = AutoTokenizer.from_pretrained(path)
    self.model_question_answering = AutoModelForQuestionAnswering.from_pretrained(path)

  def xlmr_predict(self,context, question):
    inputs = self.tokenizer(question, context, 
                       add_special_tokens=True, 
                       return_tensors='pt')
    input_ids = inputs['input_ids'].tolist()[0]

    outputs = self.model_question_answering(**inputs)
    
    # used to compute score
    start = outputs[0].detach().numpy()
    end = outputs[1].detach().numpy()

    # Generate mask
    undesired_tokens = inputs['attention_mask']
    undesired_tokens_mask = undesired_tokens == 0.0

    # Make sure non-context indexes in the tensor cannot contribute to the softmax
    start_ = np.where(undesired_tokens_mask, -10000.0, start)
    end_ = np.where(undesired_tokens_mask, -10000.0, end)

    # Normalize logits and spans to retrieve the answer
    start_ = np.exp(start_ - np.log(np.sum(np.exp(start_), axis=-1, keepdims=True)))
    end_ = np.exp(end_ - np.log(np.sum(np.exp(end_), axis=-1, keepdims=True)))

    # Compute the score of each tuple(start, end) to be the real answer
    outer = np.matmul(np.expand_dims(start_, -1), np.expand_dims(end_, 1))

    # Remove candidate with end < start and end - start > max_answer_len
    max_answer_len = 400
    candidates = np.tril(np.triu(outer), max_answer_len - 1)
    scores_flat = candidates.flatten()

    idx_sort = [np.argmax(scores_flat)]
    start, end = np.unravel_index(idx_sort, candidates.shape)[1:]
    end += 1
    score = candidates[0, start, end - 1]
    start, end, score = start.item() + 1, end.item() + 1, score.item()

    answer =self.tokenizer.decode(input_ids[start:end])
    return (answer, score)