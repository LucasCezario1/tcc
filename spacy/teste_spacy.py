import spacy

nlp = spacy.load('pt_core_news_sm')

texto = "Paris é uma cidade bonita, e Nova York também é incrível. O número de telefone é 123456789, e 15"

doc = nlp(texto)

# Identificar as entidades nomeadas no texto
detalhes_entidade = [(entidade, entidade.label_) for entidade in doc.ents]

print("Identifica o que é uma localidade no texto: ", detalhes_entidade)

# Identificar palavras significativas (tokens) no texto (excluindo pontuação)
tokens_significativos = [token.orth_ for token in doc if not token.is_punct]

print("Tokenrizacao: ", tokens_significativos)


#Pegar o unico digito do texto
alpha_tokens = [token.orth_ for token in doc if token.is_digit]

print("O digitos:" , alpha_tokens)