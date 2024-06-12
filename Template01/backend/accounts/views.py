from django.http import JsonResponse
from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import authenticate, login, logout, alogin
from rest_framework.authtoken.models import Token
import json
from . import models

@csrf_exempt
def registerUser(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        username = data.get('username')
        email = data.get('email')
        password = data.get('password')

        if not (username and email and password):
            return JsonResponse({'error': 'All fields are required'}, status=400)

        if User.objects.filter(username=username).exists():
            return JsonResponse({'error': 'Username is already taken'}, status=400)

        user = User.objects.create_user(username=username, email=email, password=password)
        user.save()
        models.Profile.objects.create(id=user).save()

        token, token_created = Token.objects.get_or_create(user=user)

        # Serialize user and token data into dictionary
        user_data = {
            # 'token': token.key,
            # 'token_created': token_created,
            'username': user.username,
            # Include other user data as needed
        }

        return JsonResponse(user_data, status=200)


        # Insert code for all post operations here...

    else:
        return JsonResponse({'error': 'Only POST requests are allowed'}, status=405)

@csrf_exempt
def loginUser(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        username = data.get('username')
        password = data.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            token, token_created = Token.objects.get_or_create(user=user)

            # Serialize user and token data into dictionary
            user_data = {
                # 'token': token.key,
                # 'token_created': token_created,
                'username': user.username,
                # Include other user data as needed
            }

            return JsonResponse(user_data, status=200)
        else:
            return JsonResponse({'error': 'Invalid credentials'}, status=401)
    else:
        return JsonResponse({'error': 'Only POST requests are allowed'}, status=405)

@csrf_exempt
def logoutUser(request):
    if request.method == 'POST':
        logout(request)
        return JsonResponse({'message': "Logout successful. "}, status=200)

