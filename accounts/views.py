from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
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
    return render(request, 'accounts/signup.html', {'form': form})


@login_required(login_url='accounts:login')
def change_password(request):
    return render(request, 'accounts/pw_change.html')


@login_required(login_url='accounts:login')
def get_member(request, member_id):
    user = User.objects.get(id=member_id)
    return render(request, 'accounts/profile.html', {'get_user': user})


@login_required(login_url='accounts:login')
def update_member(request):
    return render(request, 'accounts/profile_change.html')
