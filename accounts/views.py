from django.contrib.auth import authenticate, login, get_user_model
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render, redirect

from accounts.forms import UserCreateForm


def signup(request):
    if request.method == "POST":
        form = UserCreateForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('site_home')
    else:
        form = UserCreateForm()
    return render(request, 'accounts/signup.html', {'form':form})

def change_password(request):
    return HttpResponse("비밀번호 변경 메서드 실행 상태입니다.")


def get_member(request, member_id):
    user = User.objects.get(id=member_id)
    return render(request, 'accounts/profile.html', {'user': user})