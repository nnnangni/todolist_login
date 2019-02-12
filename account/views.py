from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
# 우리가 가져온 로그인 이름을 auth_login으로 바꿔줌(이름이 중복이되니까)
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout


# Create your views here.
def signup(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save() # 유효성검사 통과하면 저장
            auth_login(request, user)
            return redirect("todos:list")
    else:
        form = UserCreationForm()
    return render(request,"account/form.html",{"form":form})
    
def login(request):
    if request.method == "POST":
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            # 사용자의 데이터를 넣어주기
            auth_login(request, form.get_user())
            return redirect("todos:list")
    else:
        form = AuthenticationForm()
    return render(request,"account/form.html",{"form":form})

def logout(request):
    auth_logout(request)
    # 로그아웃하면 로그인페이지로 가도록
    return redirect("accounts:login")