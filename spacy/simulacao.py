import spacy
import time
import psutil

# Carregar o modelo do spaCy para o idioma português
nlp = spacy.load('pt_core_news_sm')

# Definir o texto de exemplo
texto = "Bill Gates visitou a cidade de Nova York em 15 de julho de 2022 para uma conferência sobre inovação tecnológica."

# Iniciar a contagem do tempo de execução
start_time = time.time()

# Processar o texto usando spaCy
doc = nlp(texto)

# Identificar as entidades nomeadas no texto
detalhes_entidade = [(entidade, entidade.label_) for entidade in doc.ents]

# Parar a contagem do tempo de execução
end_time = time.time()

# Calcular o tempo de execução
execution_time = end_time - start_time

# Medir o uso de memória
memory_usage = psutil.Process().memory_info().rss / (1024 ** 2)  # em MB

# Imprimir as entidades nomeadas
print("Identifica o que é uma localidade no texto:", detalhes_entidade)

# Pegar o único dígito do texto
alpha_tokens = [token.orth_ for token in doc if token.is_digit]

# Imprimir o dígito
print("O dígito:", alpha_tokens)

# Imprimir métricas de tempo de execução e uso de memória
print(f"Tempo de Execução: {execution_time:.4f} segundos")
print(f"Uso de Memória: {memory_usage:.2f} MB")
