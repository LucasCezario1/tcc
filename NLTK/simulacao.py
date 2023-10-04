import time

import nltk
import psutil
from nltk import word_tokenize, pos_tag, ne_chunk
nltk.download('punkt')

# Texto de exemplo
texto = "Barack Obama was born in Honolulu, Hawaii. He served as the 44th President of the United States."

# Iniciar a contagem do tempo
start_time = time.time()


# Tokenize o texto em palavras
palavras = word_tokenize(texto)

# Part-of-speech tagging (marcação de partes do discurso)
tags = pos_tag(palavras)

# Reconhecimento de Entidades Nomeadas (NER)
entidades = ne_chunk(tags)



# Encerrar a contagem do tempo
end_time = time.time()


# Calcular o tempo de execução
execution_time = end_time - start_time


# Medir o uso de memória
memory_usage = psutil.Process().memory_info().rss / 1024  # em KB



# Exibir as entidades nomeadas identificadas no texto de forma legível
entidades.pretty_print()
print(f"Tempo de Execução: {execution_time:.2f} segundos")
print(f"Uso de Memória: {memory_usage:.2f} KB")