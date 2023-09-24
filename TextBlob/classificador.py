from textblob.classifiers import NaiveBayesClassifier

# Seu conjunto de treinamento com exemplos de sentenças classificadas como positivas e negativas
train_data = [
    ("The beer is good.", "positivo"),
    ("The hangover is horrible.", "negativo"),
]

# Crie e treine um classificador
classifier = NaiveBayesClassifier(train_data) # entede que e um negatiuvo e possitivo

# Sentenças que você deseja classificar
sentences_to_classify = [
    "The beer is amazing.",
    "But the hangover is terrible.",
]

# Classifique as sentenças
for sentence in sentences_to_classify:
    classification = classifier.classify(sentence)
    print(f"Sentence: {sentence}")
    print(f"Classification: {classification}")
