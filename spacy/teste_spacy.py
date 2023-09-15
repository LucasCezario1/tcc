import spacy

#spacy - Faz analise do texto e analisa as palavras e da um significado para elas
nlp = spacy.load('pt_core_news_sm')

texto = "Quatro romeiros morreram atropelados na rodovia Presidente Dutra enquanto seguiam para Aparecida (SP) entre a noite de ontem e madrugada de hoje. O dia 12, de Nossa Senhora Aparecida, padroeira do Brasil, é celebrado na próxima terça-feira"

doc = nlp(texto)

# Identificar as entidades nomeadas no texto
detalhes_entidade = [(entidade, entidade.label_) for entidade in doc.ents]

print("Identifica o que é uma localidade no texto: ", detalhes_entidade)

# Identificar palavras significativas (tokens) no texto (excluindo pontuação)
tokens_significativos = [token.orth_ for token in doc if not token.is_punct]

print("Palavras significativas no texto: ", tokens_significativos)


#Pegar o unico digito do texto
alpha_tokens = [token.orth_ for token in doc if token.is_digit]

print("O unico digito:" , alpha_tokens)