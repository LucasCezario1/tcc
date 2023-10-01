import spacy

nlp = spacy.load('pt_core_news_sm')

texto = "O presidente Jair Bolsonaro visitou Brasília, a capital do Brasil, em 10 de setembro de 2023."

doc = nlp(texto)

# Identificar as entidades nomeadas no texto
detalhes_entidade = [(entidade, entidade.label_) for entidade in doc.ents]

print("Identifica o que é uma localidade no texto: ", detalhes_entidade)


#Pegar o unico digito do texto
alpha_tokens = [token.orth_ for token in doc if token.is_digit]

print("O digitos:" , alpha_tokens)