from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.core.mail import EmailMessage, EmailMultiAlternatives
from django.template import Context, exceptions
from django.template.loader import get_template
from rest_framework.authtoken.models import Token
from rest_framework import status, permissions, parsers, renderers
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.status import HTTP_401_UNAUTHORIZED
from rest_framework.views import APIView
from datetime import datetime

from common.models import Newsletter
from common.serializer import UserSerializer, NewsletterSerializer, ChangePasswordSerializer
from innstal import settings


class UserCreate(APIView):
    def post(self, request):
        day = request.data['day']
        month = request.data['month']
        year = request.data['year']
        request.data['dob'] = datetime.strptime(day+'/'+month+'/'+year, "%d/%m/%Y").date()

        response = {}
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            body = 'New Account Created'
            email = EmailMessage('Account Created', body,
                                 settings.DEFAULT_FROM_EMAIL, (serializer.data.pop('email'),))
            email.content_subtype = 'html'
            response['status'] = 'success'
            response['message'] = 'User Account created successfully'
            return Response(response, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response({'message':'User not created'}, status=status.HTTP_408_REQUEST_TIMEOUT)


class Login(APIView):
    def post(self,request):
        response = {}
        email = request.data.get("email")
        password = request.data.get("password")
        if User.objects.get(email=email):
            user = User.objects.get(email=email)
            if user:
                registered_user = authenticate(username=user.username, password=password)
            else:
                response['status'] = 'failed'
                response['message'] = 'Login failed'
                return Response({"error": "Login failed"}, status=HTTP_401_UNAUTHORIZED)
            if not registered_user:
                response['status'] = 'failed'
                response['message'] = 'Login failed'
                return Response({"error": "Login failed"}, status=HTTP_401_UNAUTHORIZED)
            else:
                response['status'] = 'success'
                response['message'] = 'User logged in succesfully'
                token, _ = Token.objects.get_or_create(user=registered_user)
                response['token'] = token.key
                return Response(response)


class Logout(APIView):
    queryset = User.objects.all()
    def get(self, request, format=None):
        response = {}
        self.request.user.auth_token.delete()
        response['status'] = 'success'
        response['message'] = 'User logged out succesfully'
        return Response(response, status=status.HTTP_200_OK)


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
            email_id = serializer.data.pop('email')
            html = get_template('subscription_email.html')
            subject, from_email, to = 'Innstal Subscription Activated',settings.DEFAULT_FROM_EMAIL , email_id
            html_content = html.render()
            msg = EmailMultiAlternatives(subject, '', from_email, [to])
            msg.attach_alternative(html_content, "text/html")
            msg.send()
            response['status'] = 'success'
            response['message'] = 'Newsletter Subcription email has been sent to the email-id'
            response['newsletter'] = serializer.data
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
            serializer = NewsletterSerializer(request_data, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                response['status'] = 'success'
                response['message'] = 'Newsletter Subscription updated'
                response['newsletter'] = serializer.data
                return Response(response, status=status.HTTP_200_OK)
            else:
                response['status'] = 'failed'
                response['message'] = 'Newsletter Subscription failed'
                response['error'] = serializer.errors
                return Response(response, status=status.HTTP_400_BAD_REQUEST)
        else:
            request.data['is_subscribed'] = True
            serializer = NewsletterSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                email_id = serializer.data.pop('email')
                html = get_template('subscription_email.html')
                subject, from_email, to = 'Innstal Subscription Activated', settings.DEFAULT_FROM_EMAIL, email_id
                html_content = html.render()
                msg = EmailMultiAlternatives(subject, '', from_email, [to])
                msg.attach_alternative(html_content, "text/html")
                msg.send()
                response['status'] = 'success'
                response['message'] = 'Newsletter Subcription email sent to the email id'
                response['newsletter'] = serializer.data
                return Response(response, status=status.HTTP_201_CREATED)


class UpdatePassword(APIView):
    permission_classes = (permissions.IsAuthenticated, )

    def get_object(self, queryset=None):
        return self.request.user

    def put(self, request, *args, **kwargs):
        self.object = self.get_object()
        serializer = ChangePasswordSerializer(data=request.data)

        if serializer.is_valid():
            old_password = serializer.data.get("old_password")
            if not self.object.check_password(old_password):
                return Response({"old_password": ["Wrong password."]},
                                status=status.HTTP_400_BAD_REQUEST)
            self.object.set_password(serializer.data.get("new_password"))
            self.object.save()
            return Response(status=status.HTTP_204_NO_CONTENT)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

