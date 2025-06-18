
# accounts/views.py
from django.shortcuts import render, redirect
from .forms import SignUpForm
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # 登録後すぐログインさせる
            return redirect('dashboard')  # ダッシュボードなどへリダイレクト
    else:
        form = SignUpForm()
    return render(request, 'accounts/signup.html', {'form': form})


from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status



@login_required
def profile_view(request):
    return render(request, 'accounts/profile.html')
