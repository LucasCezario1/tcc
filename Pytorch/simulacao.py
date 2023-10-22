import torch
from transformers import BertTokenizer, BertForMaskedLM
import time
import psutil

# Carregue o tokenizador e o modelo BERT pré-treinado em Português
tokenizer = BertTokenizer.from_pretrained("neuralmind/bert-base-portuguese-cased")
model = BertForMaskedLM.from_pretrained("neuralmind/bert-base-portuguese-cased")

# Frase com a lacuna
frase = "Eu nadei hoje na [MASK]."

# Iniciar a contagem do tempo de execução
start_time = time.time()

# Tokenize a frase
tokens = tokenizer.tokenize(frase)

# Encontre a posição do [MASK] na frase
posicao_mask = tokens.index('[MASK]')

# Converta os tokens em IDs
input_ids = tokenizer.convert_tokens_to_ids(tokens)

# Realize a previsão para a lacuna
with torch.no_grad():
    outputs = model(torch.tensor([input_ids]))
    logits = outputs.logits

# Obtenha o ID do token previsto
token_previsto_id = torch.argmax(logits[0, posicao_mask]).item()

# Converta o ID do token previsto de volta para texto
token_previsto = tokenizer.convert_ids_to_tokens(token_previsto_id)

# Substitua [MASK] pelo token previsto na frase
frase_preenchida = frase.replace('[MASK]', token_previsto)

# Parar a contagem do tempo de execução
end_time = time.time()

# Calcular o tempo de execução
execution_time = end_time - start_time

# Medir o uso de memória
memory_usage = psutil.Process().memory_info().rss / (1024 ** 2)  # em MB

# Imprima a frase preenchida
print("Frase que foi digitada:", frase)
print("Frase preenchida:", frase_preenchida)

# Imprimir métricas de tempo de execução e uso de memória
print(f"Tempo de Execução: {execution_time:.4f} segundos")
print(f"Uso de Memória: {memory_usage:.2f} MB")
