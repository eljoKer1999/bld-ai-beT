from users.models import User
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .serilaizer import RegisteringUserSerializer, getUserSerializer
from .permissions import IsAuthenticated, IsSuperUser
from django.contrib.auth import authenticate, login, logout
from knox.views import LoginView
from knox.views import LogoutView
from knox.auth import TokenAuthentication
from knox.models import AuthToken


class Register (APIView):
    permission_classes=[~IsAuthenticated|IsSuperUser]

    def post (self,request):
        serializers = RegisteringUserSerializer(data=request.data)
        if not serializers.is_valid():
            return Response(serializers.errors)

        
        User.objects.create_user(username=serializers.data["username"],
                                email=serializers.data["email"],
                                password=serializers.data["password1"])
        return Response("User created successfully")


class Login (LoginView):
    permission_classes=[~IsAuthenticated]

    def post (self,request):
        username = request.data.get('username')
        password = request.data.get('password')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            serializers = getUserSerializer(user)
            token = self.get_token()
            instance, token = AuthToken.objects.create(user, token)
            return Response({"token":token,"user":serializers.data})

        return Response("Sorry Invalid Login")

class Logout (LogoutView):

    authentication_classes = [TokenAuthentication]
    permission_classes=[IsAuthenticated]

    def post (self,request):
        logout(request)
        return super(Logout, self).post(request, format=None)
