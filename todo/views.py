from django.shortcuts import render, redirect
from .forms import TodoModelForm
from django.contrib.auth.decorators import login_required
from .models import Todo
# Create your views here.
@login_required
def list(request):
    # todos = Todo.objects.all()
    todos = request.user.todo_set.all() # 현재 로그인한 사람의 정보만 볼 수 있음.
    # 전체 todo 목록이 나오는 곳
    return render(request, "todo/list.html",{"todos":todos})
    
@login_required
def create(request):
    if request.method == "POST":
        form = TodoModelForm(request.POST)
        if form.is_valid():
            todo = form.save(commit=False) # 자동으로 저장됨. (잠깐 지연하고,,)
            todo.user = request.user # 포스트, 유저, 모든 데이터를 저장하고 있음
            todo.save()
            return redirect("todos:list")
    else:
        form = TodoModelForm()
    return render(request, "todo/create.html", {"form":form})
    
