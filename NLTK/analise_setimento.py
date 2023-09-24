import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer

# Inicialize o analisador de sentimentos VADER
nltk.download('vader_lexicon')
analyzer = SentimentIntensityAnalyzer()

# Texto que você deseja analisar
texto = "No, love is never logical"

# Avalie o sentimento usando o analisador VADER
sentimento = analyzer.polarity_scores(texto)

# Determine o sentimento com base na polaridade composta
if sentimento['compound'] >= 0.05:
    sentimento_texto = "positivo"
elif sentimento['compound'] <= -0.05:
    sentimento_texto = "negativo"
else:
    sentimento_texto = "neutro"

# Imprima o resultado
print(f"Texto: {texto}")
print(f"Sentimento: {sentimento_texto}")
