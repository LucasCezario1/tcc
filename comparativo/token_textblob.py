import time

import psutil
from textblob import TextBlob

# Texto de exemplo
texto = """
Isso é uma frase: O Processamento de Linguagem Natural (NLP, na sigla em inglês) é uma subárea da inteligência artificial 
que se concentra na interação entre computadores e linguagem humana. Ele envolve a análise e a geração 
de texto em linguagem humana, permitindo que os computadores entendam, interpretem e gerem texto de maneira 
semelhante a como os humanos o fazem.
"""

# Crie um objeto TextBlob com o texto
blob = TextBlob(texto)

# Iniciar a contagem do tempo de execução
start_time = time.time()

# Realize a tokenização de palavras
palavras_tokenizadas = blob.words


# Parar a contagem do tempo de execução
end_time = time.time()

# Calcular o tempo de execução
execution_time = end_time - start_time

# Medir o uso de memória
memory_usage = psutil.Process().memory_info().rss / (1024 ** 2)  # em MB


# Imprima as palavras tokenizadas
print(palavras_tokenizadas)


# Imprimir métricas de tempo de execução e uso de memória
print(f"Tempo de Execução: {execution_time:.4f} segundos")
print(f"Uso de Memória: {memory_usage:.2f} MB")