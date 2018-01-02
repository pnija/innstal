from django.contrib.auth.models import User
from django.core.mail import EmailMessage
from rest_framework.authtoken.models import Token
from rest_framework import status
from rest_framework.compat import authenticate
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.status import HTTP_401_UNAUTHORIZED
from rest_framework.views import APIView

from common.serializer import UserSerializer
from innstal import settings


class UserCreate(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            body = 'New Account Created'
            email = EmailMessage('Account Created', body,
                                 settings.DEFAULT_FROM_EMAIL, (serializer.data.pop('email'),))
            email.content_subtype = 'html'

            try:
                email.send()
            except Exception as e:
                print(e)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response({'message':'User not created'}, status=status.HTTP_200_OK)



@api_view(["POST"])
def login(request):
    username = request.data.get("username")
    password = request.data.get("password")
    user = authenticate(username=username, password=password)
    print(user)
    if not user:
        return Response({"error": "Login failed"}, status=HTTP_401_UNAUTHORIZED)
    token, _ = Token.objects.get_or_create(user=user)
    return Response({"token": token.key})



class Logout(APIView):
    queryset = User.objects.all()

    def get(self, request, format=None):
        # simply delete the token to force a login
        self.request.user.auth_token.delete()
        return Response(status=status.HTTP_200_OK)