from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.core.mail import EmailMessage, EmailMultiAlternatives
from django.template import Context, exceptions
from django.template.loader import get_template
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode
from django.views.generic import TemplateView
from django.shortcuts import render

from rest_framework.authtoken.models import Token
from rest_framework import status, permissions, parsers, renderers
from rest_framework.decorators import api_view
from rest_framework.exceptions import ValidationError
from rest_framework.response import Response
from rest_framework.status import HTTP_401_UNAUTHORIZED
from rest_framework.viewsets import ModelViewSet
from rest_framework.views import APIView
from rest_framework import viewsets

from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.conf import settings
from .models import Blog, BusinessUserProfile, UserPlans
from datetime import datetime
from common.models import Newsletter, UserProfile

from common.serializer import UserSerializer, NewsletterSerializer, \
    ChangePasswordSerializer, UpdatePasswordSerializer, \
    UserProfileSerializer, ContactSerializer, BlogSerializer, BusinessAccountSerializer, UserPlanSerializer
from innstal import settings


class UserCreate(APIView):
    def post(self, request):
        day = request.data['day']
        month = request.data['month']
        year = request.data['year']
        request.data['dob'] = datetime.strptime(str(day)+'/'+str(month)+'/'+year, "%d/%m/%Y").date()
        response = {}
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            id = serializer.data.pop('id')
            url = {}
            url['url_value'] = request.scheme+"://"+request.META['HTTP_HOST']+"#/activate"
            url['pk'] = id
            email_id = serializer.data.pop('email')
            html = get_template('signup_confirmation_email.html')
            subject, from_email, to = 'Innstal Account Created', settings.DEFAULT_FROM_EMAIL, email_id
            html_content = html.render(url)
            msg = EmailMultiAlternatives(subject, '', from_email, [to])
            msg.attach_alternative(html_content, "text/html")
            msg.send()
            response['status'] = 'success'
            response['message'] = 'User Account created successfully'
            return Response(response, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        return Response({'message' : 'User not created'}, status=status.HTTP_408_REQUEST_TIMEOUT)


class Login(APIView):

    def post(self, request):
        response = {}
        email = request.data.get("email")
        password = request.data.get("password")
        if User.objects.get(email=email):
            user = User.objects.get(email=email)
            if user:
                if user.is_active == True:
                    registered_user = authenticate(username=user.username, password=password)
                else:
                    response['status'] = 'failed'
                    response['message'] = 'User not activated'
                    return Response(response, status=HTTP_401_UNAUTHORIZED)
            else:
                response['status'] = 'failed'
                response['message'] = 'Login failed'
                return Response(response, status=HTTP_401_UNAUTHORIZED)
                
            if not registered_user:
                response['status'] = 'failed'
                response['message'] = 'Login failed'
                return Response(response, status=HTTP_401_UNAUTHORIZED)
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


class ContactView(APIView):
    def get(self, request, *args, **kwargs):
        serializer = ContactSerializer()
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        serializer = ContactSerializer(data=request.data)
        if serializer.is_valid():
            context = serializer.data
            html_message = render_to_string('common/email.html', context)

            try:
                send_mail('Innstal : New Contact Submission',
                    '',
                    settings.DEFAULT_FROM_EMAIL,
                    ['innstaltest@gmail.com'],
                    html_message = html_message,
                    fail_silently=False
                )
            except:
                return Response({'error': 'Email Not send'}, status=status.HTTP_503_SERVICE_UNAVAILABLE)

            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class BlogListingViewSet(ModelViewSet):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer


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


class ActivateUserAccount(TemplateView):
    template_name = 'views/dashboard.html'

    def get(self,request, pk):
        response = {}
        if User.objects.filter(pk=pk):
            user = User.objects.get(pk=pk)
            user.is_active = True
            user.save()
            response['status'] = 'success'
            response['message'] = 'User Account activated'
            return render(request, self.template_name)
        else:
            response['status'] = 'failed'
            response['message'] = 'User Not found'
            return Response(response)


class ForgotPassword(APIView):
    def post(self, request):
        response = {}
        email = request.data.get('email')
        if User.objects.filter(email=email):
            context_values = {}
            user = User.objects.get(email=email)
            token = PasswordResetTokenGenerator()
            token_value = token.make_token(user)
            # uid = urlsafe_base64_encode(force_bytes(pk))
            context_values['url_value'] = request.scheme + "://" + request.META['HTTP_HOST'] + "#/change_password"
            context_values['token'] = token_value+'/'
            # context_values['uid'] = uid
            context_values['pk'] = user.pk
            html = get_template('password_reset_email.html')
            subject, from_email, to = 'Innstal', settings.DEFAULT_FROM_EMAIL, email
            html_content = html.render(context_values)
            msg = EmailMultiAlternatives(subject, '', from_email, [to])
            msg.attach_alternative(html_content, "text/html")
            msg.send()
            response['status'] = 'success'
            response['message'] = 'Email to reset password sent successfully'
            return Response(response)
        else:
            response['status'] = 'failed'
            response['message'] = 'Check the email you have entered'
            return Response(response)

class ResetPasswordCheck(TemplateView):
    template_name = 'views/dashboard.html'

    def get(self, request, pk, **kwargs):
        response = {}
        url_token = kwargs['token']
        id = pk
        # uuid = kwargs['uuid']
        if User.objects.filter(pk=id):
            user = User.objects.get(pk=id)
            token = PasswordResetTokenGenerator()
            valid_token = token.check_token(user, url_token)
            if valid_token == True:
                response['status'] = 'success'
                response['message'] = 'Url is valid'
                response['key'] = pk
                return render(request, self.template_name)
            else:
                response['status'] = 'failed'
                response['message'] = 'Url is not valid'
                return Response(response)
        else:
            response['status'] = 'failed'
            response['message'] = 'This is not a valid user'
            return Response(response)

class ChangePassword(APIView):
    def post(self, request, pk):
        response = {}
        if User.objects.filter(pk=pk):
            user = User.objects.get(pk=pk)
            if user:
                serializer = UpdatePasswordSerializer(data=request.data)
                if serializer.is_valid():
                    user.set_password(serializer.data.get("new_password"))
                    user.save()
                    response['status'] = 'success'
                    response['message'] ='User password updated'
                    return Response(response)
                else:
                    response['status'] = 'failed'
                    response['message'] = 'Could not update user password'
                return Response(response)

class UpdateUserProfile(APIView):
    permission_classes = (permissions.IsAuthenticated, )

    def put(self, request, pk):
        response = {}
        if User.objects.filter(pk=pk):
            print(request.data)
            profile = UserProfile.objects.get(user_id=pk)
            # day = request.data['day']
            # month = request.data['month']
            # year = request.data['year']
            # request.data['dob'] = datetime.strptime(day + '/' + month + '/' + year, "%d/%m/%Y").date()
            serializer = UserProfileSerializer(instance=profile, data=request.data, context={'request': request})
            if serializer.is_valid():
                serializer.save()
                response['status'] = 'success'
                response['message'] = 'User profile updated'
                return Response(response)
            else:
                response['status'] = 'failed'
                response['message'] = 'Failed to update user profile'
                response['error'] = serializer.errors
                return Response(response, status=status.HTTP_400_BAD_REQUEST)
        else:
            response['status'] = 'failed'
            response['message'] = 'User does not exist'
            return Response(response)


class GetUserProfile(APIView):
    permission_classes = (permissions.IsAuthenticated, )

    def get(self, queryset=None):
        user_profile = UserProfile.objects.get(user=self.request.user)
        serializer = UserProfileSerializer(user_profile)
        serializer.data['user'].pop('password')
        return Response(serializer.data)


class BusinessAccountRegistration(APIView):
    def post(self, request):
        response = {}
        user = request.data.get ('user')
        email = user['email']
        if any(domain in email for domain in ['gmail', 'yahoo','rediffmail','hotmail','outlook']):
            response['status'] = 'failed'
            response['message'] = 'This domain is not allowed'
            return Response(response)
        else:
            serializer = BusinessAccountSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                url = {}
                url['url_value'] = request.scheme+"://"+request.META['HTTP_HOST']+"#/activate"
                user = serializer.data.pop('user')
                email_id = None
                for key in user:
                    if key == 'email':
                        email_id = dict(user)[key]
                    if key == 'id':
                        id = dict(user)[key]
                        url['pk'] = id
                if email_id != None:
                    html = get_template('signup_confirmation_email.html')
                    subject, from_email, to = 'Innstal Business Account Created', settings.DEFAULT_FROM_EMAIL, email_id
                    html_content = html.render(url)
                    msg = EmailMultiAlternatives(subject, '', from_email, [to])
                    msg.attach_alternative(html_content, "text/html")
                    msg.send()
                    response['status'] = 'success'
                    response['message'] = 'Business Account created successfully'
                    return Response(response, status=status.HTTP_200_OK)
                else:
                    return Response({'message': 'Account not created'}, status=status.HTTP_408_REQUEST_TIMEOUT)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            return Response({'message':'Account not created'}, status=status.HTTP_408_REQUEST_TIMEOUT)


class SelectPricingPlan(APIView):
    def get(self, request, plan_id):
        response = {}
        print(request.user.id)
        pricing_plan = UserPlans.objects.create(user_id=request.user.id, pricing_plan_id=plan_id)
        if pricing_plan:
            response['status'] = 'success'
            response['message'] = 'Selected Pricing plan for user'
            return Response(response)
        else:
            response['status'] = 'failed'
            response['message'] = 'Could  not select plan for user'
            return Response(response)


class UpdatePricingPlan(APIView):
    permission_classes = (permissions.IsAuthenticated, )
    def post(self, request, pk):
        response = {}
        pricing_plan = UserPlans.objects.get(pk=pk)
        if pricing_plan:
            pricing_plan.pricing_plan_id = request.data.get('plan_id')
            pricing_plan.save()
            response['status'] = 'success'
            response['message'] = 'Updated pricing plan for user'
            return Response(response)
        else:
            response['status'] = 'failed'
            response['message'] = 'Could  not update plan for user'
            return Response(response)


