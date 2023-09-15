import tensorflow as tf
from transformers import BertTokenizer, TFBertForTokenClassification

#Faz analise do texto e imprime o tonkens que cada palavra

# Carregue o tokenizador e o modelo BERT pré-treinado
tokenizer = BertTokenizer.from_pretrained("bert-base-multilingual-cased")
model = TFBertForTokenClassification.from_pretrained("bert-base-multilingual-cased")

# Texto de exemplo
texto = "O Brasil é conhecido por suas praias maravilhosas."

# Tokenize o texto
tokens = tokenizer(texto, padding=True, truncation=True, return_tensors="tf")

# Faça uma previsão com o modelo
predictions = model(tokens["input_ids"])


# Imprima as entidades nomeadas encontradas
print(predictions)
