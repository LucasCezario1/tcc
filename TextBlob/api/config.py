import re
import tweepy
from tweepy import OAuthHandler
from textblob import TextBlob

# insira suas credenciais de API do Twitter aqui
consumer_key = "Khs7e3FlQZJQr9hMrsIOhTdCu"
consumer_secret = "AfRovqELWwkF5EbyLn7TNykncnYsEnsa99oktTbVP6IVEkWWUT"
access_token = "1243685469017329668-7BGVel5n7qwRi9DmNoZXFxc5lHTPiZ"
access_token_secret = "S9h0rGC8GaXQ2RU36KXA2571t8SPUppm8olvwKnC1eN1v"

# autenticação com a API do Twitter
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

# criação de um objeto API
api = tweepy.API(auth)


#AAAAAAAAAAAAAAAAAAAAACdWqAEAAAAAIaW7%2FppJYUMDDtEDYlQOELsRYps%3DIey5IQzk8nqgNy3i4t03OO6OLSOS4OMuTSnpkGF0lwR234OEgj