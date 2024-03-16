import numpy as np
import pandas as pd
import spacy
from textblob import TextBlob
from spacytextblob.spacytextblob import SpacyTextBlob
nlp = spacy.load('en_core_web_sm')
nlp.add_pipe('spacytextblob') 

def preprocess(text):  #preprocessing function
  doc = nlp(text.lower().strip())
  return ' '.join([token.lemma_.lower() for token in doc if not token.is_stop and not token.is_punct])

def analyze_polarity(text):
  doc = nlp(text)
  blob = TextBlob(text)
  polarity = blob.sentiment.polarity
  return polarity

def spacy_polarity(text):

    doc = nlp(text)
    rep = doc
    polarity_value = doc._.blob.polarity
    return polarity_value

my_data = pd.read_csv("amazon_product_reviews.csv", sep =",", low_memory=False)
reviews_list = my_data[["id", "name", "reviews.text", "reviews.title"]]
test_review = reviews_list.iloc[0:5, : ]
test_review.dropna(inplace=True, axis=0)
test_review["processed_reviews"] = test_review["reviews.text"].apply(preprocess)
data = test_review['processed_reviews']
analysis = {}
for i in range(len(data)):
    my_sentence = data[i]
    print(my_sentence)
    val = spacy_polarity(my_sentence)
    polarity_score = analyze_polarity(my_sentence)
    analysis[my_sentence]=str(val)
    if polarity_score > 0:
        sentiment = ' positive'
    elif polarity_score < 0:
        sentiment = ' negative'
    else:
        sentiment = ' neutral'
    analysis[my_sentence]+=sentiment
      
print(analysis)