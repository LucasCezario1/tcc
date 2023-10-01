from textblob import TextBlob
from textblob.classifiers import NaiveBayesClassifier

# Dados de treinamento
treinamento = [
    ('Este é um ótimo filme!', 'positivo'),
    ('Que filme terrível, não gostei.', 'negativo'),
    ('Eu amei o elenco deste filme.', 'positivo'),
    ('O enredo foi confuso e entediante.', 'negativo')
]

# Crie um classificador Naive Bayes
classificador = NaiveBayesClassifier(treinamento)

# Texto de teste
texto = "Eu realmente gostei deste filme."

# Classificar o texto
categoria = classificador.classify(texto)
print("Categoria do texto:", categoria)
