import sys
from django.contrib.auth import login as auth_login, logout as auth_logout
from django.shortcuts import redirect
from django.contrib.auth import authenticate, login
from django.http import HttpResponse


# def login(request):
#     print('login view', file=sys.stderr)
#     # user = PersonaAuthenticationBackend().authenticate(request.POST['assertion'])
#     user = authenticate(assertion=request.POST['assertion'])
#     if user is not None:
#         auth_login(request, user)
#     return redirect('/')
#
# 
# def logout(request):
#     auth_logout(request)
#     return redirect('/')


def persona_login(request):
    user = authenticate(assertion=request.POST['assertion'])
    if user:
        login(request, user)
    return HttpResponse('OK')
