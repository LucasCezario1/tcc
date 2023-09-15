from textblob import TextBlob

#Analise de sentimento

texto = "I hate you "
blob = TextBlob(texto) # biblioteca que faz a analise da frase


#A sentiment propriedade retorna uma tupla nomeada no formato .
# A pontuação de polaridade é flutuante dentro do intervalo [-1,0, 1,0].
# A subjetividade é uma flutuação dentro do intervalo [0,0, 1,0] onde 0,0 é muito objetivo e 1,0 é muito subjetivo.
# Sentiment(polarity, subjectivity)
polaridade = blob.sentiment.polarity
subjetividade = blob.sentiment.subjectivity



if polaridade > 0:
    sentimento = "positivo"
elif polaridade < 0:
    sentimento = "negativo"
else:
    sentimento = "neutro"

print("Frase que foi dita:", texto)
print(f"Sentimento: {sentimento}")
print(f"Polaridade: {polaridade}")
print(f"Subjetividade: {subjetividade}")


