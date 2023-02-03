import urllib.parse
import oauth2
import json

#preencha com suas credenciais
consumer_key = ''
consumer_secret = ''
token_key = ''
token_secret = ''

consumer = oauth2.Consumer(consumer_key, consumer_secret)
token = oauth2.Token(token_key, token_secret)
cliente = oauth2.Client(consumer, token)

query = input("Digite o que quer tuitar: ")
query_codificada = urllib.parse.quote(query, safe='')

requisicao = cliente.request('https://api.twitter.com/1.1/statuses/update.json?status=' + query_codificada,
                             method='POST')
requisicao[1].decode()
objeto = json.loads(requisicao[1].decode())

print(objeto)