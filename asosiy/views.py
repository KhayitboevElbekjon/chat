from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth import authenticate,login,logout
from .models import *
from django.contrib.auth.models import User
class Chat(View):
    def get(self,request):
        if request.user.is_authenticated:
            data={
                'data':Xabar.objects.filter(user_fk=request.user)
            }
            return render(request, 'index_chat.html',data)
        return redirect('/')
    def post(self,request):
        if request.user.is_authenticated:
            matn=request.POST.get('matn')
            Xabar.objects.create(xabar=matn,
            user_fk=request.user)
            return redirect('/chat/')
        return redirect('/')

def delete(request,pk):
    if request.user.is_authenticated:
        Xabar.objects.filter(id=pk).delete()
        return redirect('/chat/')
    return redirect('/')
class LoginView(View):
    def post(self,request):
        userr=authenticate(request,username=request.POST.get('login'),
            password=request.POST.get('parol'))
        if userr is not None:
            login(request,userr)
            return redirect('chat/')
        return redirect('/')
    def get(self,request):
        return render(request,'hemis.html')

def register(request):
    if request.method=='POST' and request.POST.get('p')==request.POST.get('cp'):
        u1=User.objects.create_user(
            username=request.POST.get('l'),
            password=request.POST.get('p')
        )
        Talaba.objects.create(
            login=request.POST.get('l'),
            parol=request.POST.get('p'),
            user_fk=u1
        )
        return redirect('/')
    return render(request,'register.html')

def Logaut(request):
    logout(request)
    return redirect('/')
