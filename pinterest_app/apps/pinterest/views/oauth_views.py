from django.shortcuts import redirect, render
from django.conf import settings
import requests

def login_view(request):
    # Redirect to Pinterest OAuth2
    client_id = '<YOUR_CLIENT_ID>'
    redirect_uri = request.build_absolute_uri('/callback/')
    scope = 'pins:read,boards:read,user_accounts:read,ads:read,catalogs:read'
    auth_url = f"https://www.pinterest.com/oauth/?response_type=code&client_id={client_id}&redirect_uri={redirect_uri}&scope={scope}"
    return redirect(auth_url)

def callback_view(request):
    code = request.GET.get('code')
    if code:
        token_url = 'https://api.pinterest.com/v5/oauth/token'
        client_id = '<YOUR_CLIENT_ID>'
        client_secret = '<YOUR_CLIENT_SECRET>'
        redirect_uri = request.build_absolute_uri('/callback/')
        payload = {
            'grant_type': 'authorization_code',
            'code': code,
            'client_id': client_id,
            'client_secret': client_secret,
            'redirect_uri': redirect_uri
        }
        response = requests.post(token_url, data=payload)
        data = response.json()
        access_token = data.get('access_token')
        request.session['access_token'] = access_token
        return redirect('dashboard')
    return render(request, 'pinterest_app/login.html', {'error': 'OAuth failed'})
