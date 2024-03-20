from django.shortcuts import redirect
from django.http import JsonResponse
import requests


def home(request) -> JsonResponse:
    return JsonResponse({"first": "home"})


auth_url_discord = ("https://discord.com/oauth2/authorize?client_id=1219631665035477082&response_type=code&redirect_uri"
                    "=http%3A%2F%2Flocalhost%3A8000%2Foauth2%2Flogin%2Fredirect&scope=identify")


def discord_login(request):
    return redirect(auth_url_discord)


def discord_login_redirect(request):
    code = request.GET.get('code')
    user = exchange_code(code)
    return JsonResponse({"user": user})


def exchange_code(code: str):
    data = {
        'client_id': '1219631665035477082',
        'client_secret': 'JCGIUHRnp8DMgSih0bZ78bptgPMYmiuD',
        'grant_type': 'authorization_code',
        'code': code,
        'redirect_uri': 'http://localhost:8000/oauth2/login/redirect',
        'scope': 'identify'
    }

    headers = {
        'Content-Type': 'application/x-www-form-urlencoded'
    }

    response = requests.post('https://discord.com/api/oauth2/token', data=data, headers=headers)
    print(response)
    credentials = response.json()
    print(credentials)

    access_token = credentials['access_token']
    response = requests.get("https://discord.com/api/v6/users/@me", headers={
        'Authorization': 'Bearer %s' % access_token
    })
    print(response)
    user = response.json()
    print(user)
    return user

