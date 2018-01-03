from django.contrib.auth.models import User
from django.core.mail import EmailMessage
from rest_framework.authtoken.models import Token
from rest_framework import status
from rest_framework.compat import authenticate
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.status import HTTP_401_UNAUTHORIZED
from rest_framework.views import APIView

from common.models import Newsletter
from common.serializer import UserSerializer, NewsletterSerializer
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
            return Response(e, status=status.HTTP_408_REQUEST_TIMEOUT)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response({'message':'User not created'}, status=status.HTTP_200_OK)



class Login(APIView):
    def post(self,request):
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
        self.request.user.auth_token.delete()
        return Response(status=status.HTTP_200_OK)


class SubcribeNewsLetter(APIView):
    def post(self, request):
        response = {}
        if Newsletter.objects.filter(email=request.data.get('email')):
            response['status'] = 'failed'
            response['message'] = 'This email is already subscribed'
            return Response(response, status=status.HTTP_200_OK)
        request_data = request.data
        request_data['is_subscribed'] = True
        serializer = NewsletterSerializer(data=request_data)
        if serializer.is_valid():
            serializer.save()
            body = 'You have subscribed to Innstal services successfully'
            email = EmailMessage('Innstal Subscription Activated', body,
                                 settings.DEFAULT_FROM_EMAIL, (serializer.data.pop('email'),))
            email.content_subtype = 'html'
            response['status'] = 'success'
            response['message'] = 'Subcription email sent to the email id'
            response['newsletter'] = serializer.data
            try:
                email.send()
            except Exception as e:
                print(e)
            return Response(response, status=status.HTTP_201_CREATED)
        else:
            response['status'] = 'failed'
            response['message'] = 'Subcription failed'
            response['error'] = serializer.errors
            return Response(response, status=status.HTTP_400_BAD_REQUEST)


class UpdateNewsLetterSubscription(APIView):
    def post(self, request):
        response = {}
        if Newsletter.objects.filter(email=request.data.get('email')):
            request_data = Newsletter.objects.get(email=request.data.get('email'))
            if request_data.is_subscribed == True:
                request_data.is_subscribed = False
            elif request_data.is_subscribed == False:
                request_data.is_subscribed = True
            instance = {}
            instance['id'] = request_data.id
            serializer = NewsletterSerializer(request_data, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                response['status'] = 'success'
                response['message'] = 'Subscription updated'
                response['newsletter'] = serializer.data
                return Response(response, status=status.HTTP_200_OK)
            else:
                response['status'] = 'failed'
                response['message'] = 'Unsubcription failed'
                response['error'] = serializer.errors
                return Response(response, status=status.HTTP_400_BAD_REQUEST)
        else:
            request.data['is_subscribed'] = True
            serializer = NewsletterSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                body = 'You have subscribed to Innstal services successfully'
                email = EmailMessage('Innstal Subscription Activated', body,
                                     settings.DEFAULT_FROM_EMAIL, (serializer.data.pop('email'),))
                email.content_subtype = 'html'
                response['status'] = 'success'
                response['message'] = 'Subcription email sent to the email id'
                response['newsletter'] = serializer.data
                try:
                    email.send()
                except Exception as e:
                    print(e)
                return Response(response, status=status.HTTP_201_CREATED)