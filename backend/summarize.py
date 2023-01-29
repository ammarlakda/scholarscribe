from transformers import pipeline
from nltk import sent_tokenize
import nltk
nltk.download('punkt')

#call summarizer 
summarizer = pipeline("summarization", model="facebook/bart-large-cnn")

def summarize(Article):
  summary = summarizer(Article, max_length=350, min_length=200, do_sample=False)
  return summary
def split_article(Article):
  #Maximum sequence length 
  K = 950
  #Total number of tokens in Document
  N = len(sent_tokenize(Article))
  sentences = sent_tokenize(Article)
  #Let I be the number of sequences of K tokens or less in Document
  I = (N/K)
  i =0
  threshold = 15
  chunks = [""] * (N//threshold + 1)
  while i < N: 
    if len(sentences[i]) > K:
      sentences[i] = summarize(sentences[i])[0]["summary_text"]
      
    chunks[i//threshold] += " " + sentences[i]
    i += 1
    
  master_string = ""

  for i in range(len(chunks)):
    temp = summarize(chunks[i])[0]["summary_text"]
    master_string += temp
  
  return master_string