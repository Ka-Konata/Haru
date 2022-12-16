import requests, secrets, webbrowser, malclient
from decouple import config as getenv
from scripts import configs


logger  = configs.logging.getLogger('discord')
class Token:
    access_token = None
    refresh_token = None


def get_new_code_verifier() -> str:
    token = secrets.token_urlsafe(100)
    return token[:128]


def print_new_authorisation_url(code_challenge: str, client_id: str):

    url = f'https://myanimelist.net/v1/oauth2/authorize?response_type=code&client_id={client_id}&code_challenge={code_challenge}'
    webbrowser.open(url=url, new=2)
    logger.info(f'Go to this url and copy the code after being redirected: {url}')


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
    logger.info('Token gererated successfully')

    return token


def print_user_info(token_obj: Token, refresh: bool = False, client_id: str = None, client_secret: str = None):
    if refresh:
        client = malclient.Client(access_token=token_obj.access_token) 
        client.refresh_bearer_token(client_id, client_secret, token_obj.refresh_token)
        user   = client.get_user_info()
        logger.info(f'Logged as: {user.name}')

    else:
        url = 'https://api.myanimelist.net/v2/users/@me'
        response = requests.get(url, headers = {
            'Authorization': f'Bearer {token_obj.access_token}'
            })
        
        response.raise_for_status()
        user = response.json()
        response.close()

        logger.info(f'Logged as: {user["name"]}')


def get_token(client_id: str, client_secret: str) -> Token:
    # Cheking if is necessary to get a new token
    try:
        logger.info('Trying to get stored token')
        token_obj = Token
        token_obj.access_token  = getenv('MAL_ACCESS_TOKEN')
        token_obj.refresh_token = getenv('MAL_REFRESH_TOKEN')
        print_user_info(token_obj, refresh=True, client_id=client_id, client_secret=client_secret)
        return token_obj
    except:
        logger.error('Invalid token entered')

    logger.info('Entering the App Login Interface (MAL)')
    logger.info('My Anime List: App Login Interface')
    code_verifier = code_challenge = get_new_code_verifier()
    print_new_authorisation_url(code_challenge, client_id)

    authorisation_code = input('Paste the code here > ').strip()
    token = generate_new_token(authorisation_code, code_verifier, client_id, client_secret)

    token_obj                       = Token
    token_obj.access_token          = token['access_token']
    token_obj.refresh_token         = token['refresh_token']
    
    with open('.env', 'r+') as f:
        old = f.read()
        if not 'MAL' in str(old):
            M1 = f'\nMAL_ACCESS_TOKEN={token_obj.access_token}'
            M2 = f'\nMAL_REFRESH_TOKEN={token_obj.refresh_token}'
            f.writelines(M1 + M2)

    return token_obj
