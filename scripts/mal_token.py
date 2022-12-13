import json
import requests
import secrets
import webbrowser
from decouple import config as getenv


def get_new_code_verifier() -> str:
    token = secrets.token_urlsafe(100)
    return token[:128]


def print_new_authorisation_url(code_challenge: str, client_id: str):

    url = f'https://myanimelist.net/v1/oauth2/authorize?response_type=code&client_id={client_id}&code_challenge={code_challenge}'
    webbrowser.open(url=url, new=2)
    print(f'GO TO: {url}\n'+'-'*110+'\n')


def generate_new_token(authorisation_code: str, code_verifier: str, client_id: str, client_secret: str) -> dict:

    url = 'https://myanimelist.net/v1/oauth2/token'
    data = {
        'client_id': client_id,
        'client_secret': client_secret,
        'code': authorisation_code,
        'code_verifier': code_verifier,
        'grant_type': 'authorization_code'
    }

    response = requests.post(url, data)
    response.raise_for_status()

    token = response.json()
    response.close()
    print('TOKEN GENERATED SUCCESSFULLY')

    #with open('token.json', 'w') as file:
    #    json.dump(token, file, indent = 4)
    #    print('TOKEN SAVED AT: "token.json"')

    return token


def print_user_info(access_token: str):
    url = 'https://api.myanimelist.net/v2/users/@me'
    response = requests.get(url, headers = {
        'Authorization': f'Bearer {access_token}'
        })
    
    response.raise_for_status()
    user = response.json()
    response.close()

    print(f"LOGGED AS {user['name']}!")


def get_token(client_id: str, client_secret: str):
    print('MY ANIME LIST: APP LOGIN INTERFACE')
    code_verifier = code_challenge = get_new_code_verifier()
    print_new_authorisation_url(code_challenge, client_id)

    authorisation_code = input('PASTE THE CODE HERE ').strip()
    token = generate_new_token(authorisation_code, code_verifier, client_id, client_secret)

    class Token:
        access_token = token['access_token']
        refresh_token = token['refresh_token']

    print_user_info(token['access_token'])
    return Token