import time

import psutil
from textblob import TextBlob

#Analise de sentimento

# algumas abigudades ele nao entede como shame ele coloca como neutro
texto = "I am love you"
blob = TextBlob(texto) # biblioteca que faz a analise da frase

# Iniciar a contagem do tempo de execução
start_time = time.time()


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


# Parar a contagem do tempo de execução
end_time = time.time()


# Medir o uso de memória
memory_usage = psutil.Process().memory_info().rss / (1024 ** 2)  # em MB



# Calcular o tempo de classificação
# Calcular o tempo de execução
execution_time = end_time - start_time


print("Frase que foi dita:", texto)
print(f"Sentimento: {sentimento}")
print(f"Polaridade: {polaridade}")
print(f"Subjetividade: {subjetividade}")

print(f"Tempo: {execution_time:.4f} segundos")
print(f"Uso de Memória: {memory_usage:.2f} MB")

