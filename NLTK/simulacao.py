import nltk
from nltk import word_tokenize, pos_tag, ne_chunk

# Baixe os recursos necessários (se ainda não tiver feito isso)
nltk.download('punkt')
nltk.download('maxent_ne_chunker')
nltk.download('words')

# Texto de exemplo
texto = "Pela proposta, os povos indígenas só poderão reivindicar a posse de áreas que ocupavam, de forma permanente, em 5 de outubro de 1988, data da promulgação da Constituição. Na prática, se as comunidades não comprovarem que estavam nas terras nesta data, poderão ser expulsas."

# Tokenize o texto em palavras
palavras = word_tokenize(texto)

# Part-of-speech tagging (marcação de partes do discurso)
tags = pos_tag(palavras)

# Reconhecimento de Entidades Nomeadas (NER)
entidades = ne_chunk(tags)

# Função para extrair e formatar entidades nomeadas
def extrair_entidades_nomeadas(tree):
    entidades = []
    for subtree in tree:
        if type(subtree) == nltk.Tree:
            label = subtree.label()
            nome = " ".join([word for word, tag in subtree.leaves()])
            entidades.append((nome, label))
    return entidades

# Exibir as entidades nomeadas e suas categorias
entidades_nomeadas = extrair_entidades_nomeadas(entidades)
print("Identifica o que é uma localidade no texto:", entidades_nomeadas)
