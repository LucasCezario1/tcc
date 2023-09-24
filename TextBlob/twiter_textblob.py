import tweepy


import tweepy
from textblob import TextBlob

#Erro ao postar o tweet: 403 Forbidden
        # Configurar as credenciais da API do Twitter
consumer_key  = "Khs7e3FlQZJQr9hMrsIOhTdCu"
consumer_secret= "AfRovqELWwkF5EbyLn7TNykncnYsEnsa99oktTbVP6IVEkWWUT"
access_token= "1243685469017329668-7BGVel5n7qwRi9DmNoZXFxc5lHTPiZ"
access_token_secret = "S9h0rGC8GaXQ2RU36KXA2571t8SPUppm8olvwKnC1eN1v"


auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

# Crie uma mensagem de tweet que você deseja postar
tweet = "Estou muito feliz hoje! 😃"  # Sua mensagem de tweet

# Realize a análise de sentimento usando o TextBlob
blob = TextBlob(tweet)
sentimento = blob.sentiment

# Determine o sentimento (positivo, negativo ou neutro)
if sentimento.polarity > 0:
    sentimento_texto = "positivo"
elif sentimento.polarity < 0:
    sentimento_texto = "negativo"
else:
    sentimento_texto = "neutro"

# Poste o tweet no Twitter
try:
    api.update_status(f"{tweet} (Sentimento: {sentimento_texto})")
    print("Tweet publicado com sucesso!")
except  tweepy.errors.TweepyException as e:
    print(f"Erro ao postar o tweet: {str(e)}")
