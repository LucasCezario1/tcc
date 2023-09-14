from transformers import AutoTokenizer, AutoModelForSeq2SeqLM, pipeline


def main():
    #  huggingface
    tokenizer = AutoTokenizer.from_pretrained("unicamp-dl/translation-pt-en-t5")
    model = AutoModelForSeq2SeqLM.from_pretrained("unicamp-dl/translation-pt-en-t5")
    enpt_pipeline = pipeline('text2text-generation', model=model, tokenizer=tokenizer)

    source_text = "E você quer dizer todas aquelas palavras que você disse"
    translated_text = enpt_pipeline("translate English to Portuguese: " + source_text)

    print("Texto de origem (português):", source_text)
    print("Tradução (ingles):", translated_text[0]['generated_text'])


if __name__ == "__main__":
    main()
