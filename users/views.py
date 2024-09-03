from django.shortcuts import HttpResponse
from django.contrib.auth.models import User
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.exceptions import NotAuthenticated
from .models import Profile

class UserAPI(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [AllowAny]

    def get(self, request):
        user = request.user
        if not user.is_authenticated:
            raise NotAuthenticated()
        profile = Profile.objects.get(user=user)
        return Response({
            "username": user.username,
            "first_name": user.first_name,
            "last_name": user.last_name,
            "email": user.email,
            "bio": profile.bio,
        })

    def post(self, request):
        username = request.data.get("username", "")
        password = request.data.get("password", "")
        first_name = request.data.get("first_name", "")
        last_name = request.data.get("last_name", "")
        email = request.data.get("email", "")
        bio = request.data.get("bio", "")

        if username and password:
            if User.objects.filter(username=username).exists():
                return Response({
                    "error": "A user with that username exists",
                }, status=401)
            if len(password) < 8:
                return Response({
                    "error": "Password is too short! Your password must be at least 8 characters!"
                })

            user = User.objects.create_user(username=username, password=password, first_name=first_name, last_name=last_name, email=email)
            profile = Profile.objects.create(
                user=user,
                bio=bio,
            )
            refresh = RefreshToken.for_user(user)
            return Response({
                "refresh": str(refresh),
                'access': str(refresh.access_token),
                "profile": {
                    "bio": profile.bio
                }
            }, status=201)

        return Response({
            "error": "Both username and password must be provided."
        })


def home(request):
    return HttpResponse("Namaste")