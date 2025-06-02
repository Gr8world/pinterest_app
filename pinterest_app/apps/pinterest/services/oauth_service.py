import requests
from django.conf import settings

def exchange_code_for_token(code, redirect_uri):
    token_url = 'https://api.pinterest.com/v5/oauth/token'
    client_id = settings.PINTEREST_CLIENT_ID
    client_secret = settings.PINTEREST_CLIENT_SECRET
    payload = {
        'grant_type': 'authorization_code',
        'code': code,
        'client_id': client_id,
        'client_secret': client_secret,
        'redirect_uri': redirect_uri
    }
    response = requests.post(token_url, data=payload)
    return response.json()

def fetch_user_profile(token):
    url = 'https://api.pinterest.com/v5/user_account'
    headers = {'Authorization': f'Bearer {token}'}
    response = requests.get(url, headers=headers)
    return response.json()
