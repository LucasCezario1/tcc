
# SpaCy
import spacy
nlp = spacy.load('en_core_web_sm')

text = "Este é um teste de tokenização com NLTK."
doc = nlp(text)
tokens = [token.text for token in doc]
print(tokens)