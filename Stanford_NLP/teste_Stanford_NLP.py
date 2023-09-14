from stanfordcorenlp import StanfordCoreNLP

# Inicialize o objeto StanfordCoreNLP com o servidor local
nlp = StanfordCoreNLP(r'stanford-corenlp-full-2021-08-01', lang='pt')

# Texto de exemplo para sumarização
texto = """
A inteligência artificial (IA) é um campo da ciência da computação que se concentra na criação de sistemas que podem executar tarefas que normalmente exigiriam inteligência humana. 
Esses sistemas podem realizar tarefas como reconhecimento de fala, processamento de linguagem natural, visão computacional e muito mais.
"""

# Realize a sumarização
sumarizacao = nlp.annotate(texto, properties={
    'annotators': 'tokenize,ssplit,pos,lemma,ner,parse,sentiment,depparse,natlog,openie',
    'pipelineLanguage': 'pt',
    'outputFormat': 'json'
})

# Imprima a sumarização
print(sumarizacao)

# Encerre o objeto StanfordCoreNLP
nlp.close()
