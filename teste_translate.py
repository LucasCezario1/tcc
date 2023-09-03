from translate import Translator

def main():
    translator = Translator(to_lang="pt")
    translation = translator.translate("I like to eat rice.") # nao traduz a palavra arroz com essa biblioteca
    print(translation)

if __name__ == '__main__':
    main()