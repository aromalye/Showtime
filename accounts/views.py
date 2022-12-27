from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Account
from django.views import View
from .serializers import AccountSerializer
from .forms import RegisterForm, LoginForm

# Create your views here.
class UserRegister(View):
    form_class = RegisterForm
    initial = {'key': 'value'}
    template_name = 'accounts/register.html'

    def get(self, request, *args, **kwargs):
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            password = form.cleaned_data['password']
            user = form.save(commit=False)
            user.set_password(password)
            user.save()
            return HttpResponse("done bro")
        return render(request, self.template_name, {'form': form})


class UserLogin(View):
    form_class = LoginForm
    initial = {'key': 'value'}
    template_name = 'accounts/login.html'

    def get(self, request, *args, **kwargs):
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'form': form})
    
    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            print(password)

            user = authenticate(request, username=email, password=password)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect('index')
                else:
                    return HttpResponse("disabled account")
            else:
                return HttpResponse("invalid login")
        return render(request, self.template_name, {'form': form})

def userlogout(request):
    logout(request)
    return redirect('index')

#through api
@api_view(['POST'])
def register_user(request):
    data = request.data
    password = data['password']
    confirm_password = data['confirm_password']
    username = data['username']
    email = data['email']
    first_name = data['first_name']
    last_name = data['first_name']
    if password == confirm_password:
        is_email_taken = Account.objects.filter(email=email).exists()
        is_username_taken = Account.objects.filter(username=username).exists()
        if not is_email_taken:
            if not is_username_taken:
                user = Account.objects.create_user(
                    first_name=first_name,
                    last_name=last_name,
                    username=username,
                    email=email,
                    password=password
                )
                user.save()
                serializer = AccountSerializer(user, many=False)
                return Response(serializer.data)
            else:
                response = Response()
                response.data = {
                    'error': 'email already taken' 
                }
                return response
        else:
            response = Response()
            response.data = {
                'error': 'email already taken' 
            }
            return response
    else:
        response = Response()
        response.data = {
            'error': 'password doesnt match' 
        }
        return response
