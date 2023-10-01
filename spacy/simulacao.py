import spacy

nlp = spacy.load('pt_core_news_sm')

texto = "Bill Gates visitou a cidade de Nova York em 15 de julho de 2022 para uma conferência sobre inovação tecnológica."

doc = nlp(texto)

# Identificar as entidades nomeadas no texto
detalhes_entidade = [(entidade, entidade.label_) for entidade in doc.ents]

print("Identifica o que é uma localidade no texto: ", detalhes_entidade)


#Pegar o unico digito do texto
alpha_tokens = [token.orth_ for token in doc if token.is_digit]

print("O digitos:" , alpha_tokens)