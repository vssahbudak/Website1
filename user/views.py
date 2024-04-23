from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib import messages

# Create your views here.

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            messages.add_message(request,messages.SUCCESS,'Oturum acma basarılı')
            return redirect('index')
        else:
            messages.add_message(request,messages.ERROR,'BAŞARISIZ')
            return redirect('login')
    else: #method POST degilse ilk defa cagrılan sayfa
        return render( request, 'user/login.html')

def register(request):
    if request.method == 'POST':
        username =  request.POST['username']
        email =  request.POST['email']
        password =  request.POST['password']
        repassword = request.POST['repassword']

        if password==repassword :
            if User.objects.filter(username = username).exists():
                messages.add_message(request,messages.WARNING,'Kullanıcı adı alınmıs')
                return redirect('register')
            else:
                if User.objects.filter(email=email).exists():
                    messages.add_message(request,messages.WARNING,'Eposta adresi alınmıs')
                    return redirect('register')
                else:
                    user = User.objects.create_user(username=username,password=password,email=email)
                    user.save()
                    print('Kullanıcı olusturuldu')
                    return redirect('login')
        else:
            print('Parola eşleşmiyor')
            return redirect('register')
    else:
        return render(request,'user/register.html')

def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        messages.add_message(request,messages.SUCCESS,'Çıkıs basarılı')
        return redirect('login')