from transformers import AutoTokenizer, AutoModelForSeq2SeqLM, pipeline


def main():
    tokenizer = AutoTokenizer.from_pretrained("unicamp-dl/translation-en-pt-t5")
    model = AutoModelForSeq2SeqLM.from_pretrained("unicamp-dl/translation-en-pt-t5")
    enpt_pipeline = pipeline('text2text-generation', model=model, tokenizer=tokenizer)

    source_text = "I like to eat rice."
    translated_text = enpt_pipeline("translate English to Portuguese: " + source_text)

    print("Texto de origem (inglês):", source_text)
    print("Tradução (português):", translated_text[0]['generated_text'])


if __name__ == "__main__":
    main()
