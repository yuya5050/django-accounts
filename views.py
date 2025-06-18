
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
"""from django.contrib.auth.decorators import login_required

@login_required
def dashboard(request):
    # ログイン済みユーザーだけアクセスできるページ
    return render(request, 'dashboard.html')"""

#apiの使用例です。pip install djangorestframeworkが必要です。
#curl -X POST "http://localhost:8000/api/echo/" -H "Content-Type: application/json" -d "{\"name\": \"Alice\", \"age\": 25}"

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

@api_view(['POST'])
def echo_api(request):
    # POSTで送られてきたJSONデータをそのまま返す
    data = request.data
    if not data:
        return Response({"error": "データがありません"}, status=status.HTTP_400_BAD_REQUEST)
    return Response({"received_data": data}, status=status.HTTP_200_OK)


@login_required
def profile_view(request):
    return render(request, 'accounts/profile.html')