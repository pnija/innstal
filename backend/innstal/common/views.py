from rest_framework.authtoken.models import Token
from rest_framework import status
from rest_framework.compat import authenticate
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.status import HTTP_401_UNAUTHORIZED
from rest_framework.views import APIView

from common.serializer import UserSerializer


class UserCreate(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        response = []
        if serializer.is_valid():
            user = serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response({'message':'User not created'}, status=status.HTTP_200_OK)



@api_view(["POST"])
def login(request):
    username = request.data.get("username")
    password = request.data.get("password")
    user = authenticate(username=username, password=password)
    if not user:
        return Response({"error": "Login failed"}, status=HTTP_401_UNAUTHORIZED)
    token, _ = Token.objects.get_or_create(user=user)
    return Response({"token": token.key})