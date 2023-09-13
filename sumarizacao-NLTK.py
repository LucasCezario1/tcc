import nltk
from nltk.corpus import stopwords
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.probability import FreqDist
from nltk.tokenize.treebank import TreebankWordDetokenizer

# NLTK

# Baixe os recursos necessários (somente uma vez)
nltk.download('punkt')
nltk.download('stopwords') #remove as palavras que sao inrelevantes

# Função para realizar a sumarização
def sumarizacao_text(text, num_sentences=2):
    # Tokenize o texto em frases e palavras
    senteacas = sent_tokenize(text)
    palvaras = word_tokenize(text)

    # Remova palavras de parada (stop palvaras)
    stop_palvaras = set(stopwords.words('portuguese'))
    palvaras = [word.lower() for word in palvaras if word.isalnum() and word.lower() not in stop_palvaras]

    # Calcule a frequência das palavras
    freq_dist = FreqDist(palvaras)

    # Obtenha as palavras mais frequentes
    mais_comum_palvaras = freq_dist.most_common(num_sentences)

    # Crie a sumarização
    sumario_sentences = []
    for word, freq in mais_comum_palvaras:
        for sentecas in senteacas:
            if word in sentecas.lower():
                sumario_sentences.append(sentecas)
                break

    # Detokenize as frases para criar o resumo final
    sumario_texto = TreebankWordDetokenizer().detokenize(sumario_sentences)

    return sumario_texto

# Texto de exemplo
text = """
A Inteligência Artificial (IA) é um campo da ciência da computação que busca criar sistemas que possam executar tarefas que normalmente requerem inteligência humana. Essas tarefas incluem reconhecimento de fala, processamento de linguagem natural e visão computacional. A IA tem aplicações em diversas áreas, como assistentes virtuais, carros autônomos e diagnóstico médico.

O processamento de linguagem natural (PLN) é uma subárea da IA que se concentra na interação entre computadores e linguagem humana. Ele envolve a análise e a geração de texto em linguagem natural. A sumarização de texto é uma técnica do PLN que envolve a criação de um resumo conciso e informativo de um texto mais longo.

Existem várias abordagens para a sumarização de texto, incluindo a extração das frases mais importantes do texto ou a geração de frases resumidas com base no conteúdo. A biblioteca NLTK é uma ferramenta útil para implementar técnicas de PLN, como a sumarização de texto.
"""

# Realize a sumarização
sumario = sumarizacao_text(text)
print("Resultado do resumo do texto:", sumario)
