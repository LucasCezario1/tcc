import time

import psutil

import spacy

# Carregue o modelo spaCy (por exemplo, para o idioma inglês)
nlp = spacy.load("pt_core_news_sm")

# Texto de exemplo
texto = """
Isso é uma frase: O Processamento de Linguagem Natural (NLP, na sigla em inglês) é uma subárea da inteligência artificial 
que se concentra na interação entre computadores e linguagem humana. Ele envolve a análise e a geração 
de texto em linguagem humana, permitindo que os computadores entendam, interpretem e gerem texto de maneira 
semelhante a como os humanos o fazem.
"""

# Iniciar a contagem do tempo de execução
start_time = time.time()

# Tokenize o texto com spaCy
doc = nlp(texto)


# Processar tokens com PyTorch
tokens_processados = [token.text for token in doc]
# Agora, você pode prosseguir com o processamento de tokens usando PyTorch, se necessário.


# Parar a contagem do tempo de execução
end_time = time.time()

# Calcular o tempo de execução
execution_time = end_time - start_time

# Medir o uso de memória
memory_usage = psutil.Process().memory_info().rss / (1024 ** 2)  # em MB

# Imprima os tokens processados
print(tokens_processados)



# Imprimir métricas de tempo de execução e uso de memória
print(f"Tempo de Execução: {execution_time:.4f} segundos")
print(f"Uso de Memória: {memory_usage:.2f} MB")