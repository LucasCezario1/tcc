import nltk
from nltk.tokenize import word_tokenize

nltk.download('corpora')
nltk.download('punkt')

text = "NLTK is a powerful library for natural language processing."
tokens = word_tokenize(text)
print(tokens)

