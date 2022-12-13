import malclient, scripts.mal_token as mal_token
from decouple import config as getenv

CLIENT_ID = getenv('CLIENT_ID')
CLIENT_SECRET = getenv('CLIENT_SECRET')

token = mal_token.get_token(CLIENT_ID, CLIENT_SECRET)
client = malclient.Client(access_token=token.access_token, nsfw=True) 

while True:
    client.refresh_bearer_token(CLIENT_ID, CLIENT_SECRET, token.refresh_token)
    key = str(input('>> '))
    search = client.get_user_anime_list()

    c = 0
    for anime in search:
        print(f'{c}- {anime}')
        c += 1
