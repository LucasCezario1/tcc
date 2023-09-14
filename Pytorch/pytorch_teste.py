import torch
from transformers import BertTokenizer, BertForMaskedLM

# Carregue o tokenizador e o modelo BERT pré-treinado em Português
tokenizer = BertTokenizer.from_pretrained("neuralmind/bert-base-portuguese-cased")
model = BertForMaskedLM.from_pretrained("neuralmind/bert-base-portuguese-cased")

# Frase com a lacuna
frase = "Tinha uma [MASK] no meio do caminho."

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

# Converta o ID do token previsto de volta para texto basicamente converte para string
token_previsto = tokenizer.convert_ids_to_tokens(token_previsto_id)

# Substitua [MASK] pelo token previsto na frase
frase_preenchida = frase.replace('[MASK]', token_previsto)

# Imprima a frase preenchida
print("Frase preenchida:", frase_preenchida)
