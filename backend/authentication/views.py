import random
import string

from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.utils import timezone
from rest_framework import permissions
from rest_framework.decorators import api_view
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.authentication import JWTAuthentication

from .models import EmailConfirmationRequests


def generate_n_char_code(n: int):
    """Generates a 6 char code (numbers and letters)

    Parameters
    ----------
    n : int
        Number of characters to generate

    Returns
    -------
    str
        A string with n characters
    """
    code = "".join(
        random.choice(string.ascii_letters + string.digits) for _ in range(n)
    )
    return code.upper()


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
            is_active=False,
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


@api_view(["POST"])
def send_email_confirmation(request: Request):
    """
    Send an email to confirm the user's email.
    """
    email = request.data["email"]
    six_char_code = generate_n_char_code(6)
    body = f"Use o código {six_char_code} para confirmar seu email."

    # In case the user already has an email confirmation request
    if EmailConfirmationRequests.objects.filter(email=email).exists():
        email_confirmation_request = EmailConfirmationRequests.objects.get(email=email)
        email_confirmation_request.code = six_char_code
        email_confirmation_request.expires_at = timezone.now() + timezone.timedelta(
            hours=12
        )
        email_confirmation_request.save()
    else:
        EmailConfirmationRequests.objects.create(
            user=User.objects.get(email=email),
            email=email,
            code=six_char_code,
        )

    send_mail(
        "ATUS - Confirmação de e-mail",
        body,
        None,
        [email],
        fail_silently=False,
    )

    return Response(status=200)


@api_view(["POST"])
def confirm_email(request: Request):
    """Confirm the user's email."""
    email = request.data["email"]
    code = request.data["code"]

    if not EmailConfirmationRequests.objects.filter(email=email).exists():
        return Response({"message": "Email não cadastrado!"}, status=400)

    email_confirmation_request = EmailConfirmationRequests.objects.get(email=email)

    if email_confirmation_request.code != code:
        return Response({"message": "Código inválido!"}, status=400)
    elif email_confirmation_request.expires_at < timezone.now():
        return Response({"message": "Código expirado!"}, status=400)

    email_confirmation_request.delete()
    user = User.objects.get(email=email)
    user.is_active = True
    user.save()

    return Response({"message": "Email confirmado com sucesso!"}, status=200)
