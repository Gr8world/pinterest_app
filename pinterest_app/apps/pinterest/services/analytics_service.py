import requests
from django.conf import settings

BASE_URL = "https://api.pinterest.com/v5"

def get_pin_analytics(token, pin_id):
    url = f"{BASE_URL}/pins/{pin_id}/analytics"
    headers = {"Authorization": f"Bearer {token}"}
    response = requests.get(url, headers=headers)
    return response.json()

def get_audience_insights(token):
    url = f"{BASE_URL}/ads/audiences/insights"
    headers = {"Authorization": f"Bearer {token}"}
    response = requests.get(url, headers=headers)
    return response.json()
