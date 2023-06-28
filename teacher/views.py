from rest_framework import generics, permissions, views
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.request import Request
from rest_framework.response import Response

from .serializers import LoginSerializer, RegistrationSerializer


class RegistrationView(generics.CreateAPIView):
    """ Чтобы зарегистрировать пользователя: Введите номер телефона и пароль """
    serializer_class = RegistrationSerializer

    def create(self, request: Request, *args, **kwargs) -> Response:
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return Response({'message': 'Thanks for registration!'})
    

class LoginView(ObtainAuthToken):
    """ Введите логин и пароль """
    serializer_class = LoginSerializer


class LogoutView(views.APIView):
    permission_classes = [permissions.IsAuthenticated]

    def delete(self, request: Request) -> Response:
        Token.objects.get(user=request.user).delete()
        return Response({'message': 'Logged out'})
    

    