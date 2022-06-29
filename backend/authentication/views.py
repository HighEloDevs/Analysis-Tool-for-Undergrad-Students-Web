from django.contrib.auth.models import User
from rest_framework import permissions
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.authentication import JWTAuthentication


class UserView(APIView):
    permission_classes = [permissions.AllowAny]

    def post(self, request: Request):
        """
        Create a new user.
        """

        username = request.data["username"]
        email = request.data["email"]

        if User.objects.filter(username=username).exists():
            return Response({"message": "Nome de usuário já existe!"}, status=400)

        elif User.objects.filter(email=email).exists():
            return Response({"message": "Email já existe!"}, status=400)

        user = User.objects.create(
            username=username,
            email=email,
            first_name=request.data["firstName"],
            last_name=request.data["lastName"],
        )
        user.set_password(request.data["password"])
        user.save()

        return Response({"message": "Usuário criado com sucesso!"}, status=200)

    def get(self, request: Request):
        """
        Get the user's data.
        """
        auth = JWTAuthentication().authenticate(request)
        if auth is None:
            return Response({"message": "Não autenticado!"}, status=400)

        user: User = auth[0]
        return Response(
            {
                "user": {
                    "username": user.username,
                    "email": user.email,
                    "first_name": user.first_name,
                    "last_name": user.last_name,
                    "is_staff": user.is_staff,
                }
            }
        )
