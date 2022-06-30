from cmath import exp
from django.conf import settings
from django.shortcuts import render, redirect
from django.urls import reverse
import requests
from rest_framework.response import Response 
from rest_framework import status
from django.http import JsonResponse

def kakaoLogin(request):
    client_id = settings.KAKAO['rest_api_key']
    redirection_uri = settings.KAKAO['callback_url']
    _url = f'https://kauth.kakao.com/oauth/authorize?client_id={client_id}&redirect_uri={redirection_uri}&response_type=code'
    return redirect(_url)

def kakaoLoginCallback(request):
    auth_code = request.GET.get('code')
    if auth_code is None:
        raise Exception("auth_code is none")

    kakao_token_api = 'https://kauth.kakao.com/oauth/token'
    data = {
        'grant_type': 'authorization_code',
        'client_id': settings.KAKAO['rest_api_key'],
        'redirection_uri': settings.KAKAO['callback_url'],
        'code': auth_code
    }

    token_response = requests.post(kakao_token_api, data=data)
    access_token = token_response.json().get('access_token')
    print("access_token ###### ",access_token)
    user_info_response = requests.get('https://kapi.kakao.com/v2/user/me', headers={"Authorization": f'Bearer ${access_token}'})

    # 회원가입 부분

    return JsonResponse({"user_info": user_info_response.json()})

def kakaoLogout(request):
    _token = request.session['access_token']
    _url = 'https://kapi.kakao.com/v1/user/logout'
    _header = {
      'Authorization': f'bearer {_token}'
    }
    _res = requests.post(_url, headers=_header)
    _result = _res.json()
    if _result.get('id'):
        del request.session['access_token']
        return JsonResponse({"result": "loginoutSuccess"}, status.HTTP_200_OK)
    else:
        return JsonResponse({'err_msg': 'email exists but not social user'}, status=status.HTTP_400_BAD_REQUEST)