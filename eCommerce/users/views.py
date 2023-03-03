from rest_framework.permissions import AllowAny
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import RegisterSerializer
from rest_framework.authtoken.models import Token
from rest_framework import generics
from rest_framework.status import (
    HTTP_400_BAD_REQUEST,
    HTTP_404_NOT_FOUND,
    HTTP_200_OK
)
from django.contrib.auth import get_user_model, authenticate

User = get_user_model()


# Create your views here.

class LoginUserAPIView(APIView):
    def post(self, request, *args, **kwargs):
        username = request.data.get('username')
        password = request.data.get('password')
        if username is None or password is None:
            return Response({'error': 'please enter username or password'}, status=HTTP_400_BAD_REQUEST)
        user = authenticate(username=username, password=password)
        if not user:
            return Response({'error': 'Invalid Credentials'},
                            status=HTTP_404_NOT_FOUND)
        token, _ = Token.objects.get_or_create(user=user)
        return Response({'token': token.key},
                        status=HTTP_200_OK)




class RegisterUserAPIView(generics.CreateAPIView):
    permission_classes = (AllowAny,)
    serializer_class = RegisterSerializer

# class UserLogin(APIView):
#     def post(self, request):
#         user_serial = LoginSerializer(data=request.data)
#         if user_serial.is_valid():
#             user_serial.save()
#             login(request, user_serial)
#             return Response(user_serial.data)
#
#
# class UserRegister(CreateAPIView):
#     permission_classes = (AllowAny,)
#     serializer_class = RegisterSerializer
