import requests
from django.conf import settings

BASE_URL = "https://api.pinterest.com/v5"

def get_user_boards(token):
    url = f"{BASE_URL}/boards"
    headers = {"Authorization": f"Bearer {token}"}
    response = requests.get(url, headers=headers)
    return response.json()

def get_pins_for_board(token, board_id):
    url = f"{BASE_URL}/boards/{board_id}/pins"
    headers = {"Authorization": f"Bearer {token}"}
    response = requests.get(url, headers=headers)
    return response.json()
