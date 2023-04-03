from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.decorators.http import require_POST

from .models import Todo
from .forms import TodoForms
# Create your views here.

def index(request):
    mytodo = Todo.objects.order_by('id')
    form = TodoForms()
    context = {'mytodo':mytodo, 'form':form}
    return render(request, "todo/index.html")

@require_POST
def addNewTodo(request):
    form = TodoForms(request.POST)

    if form.is_valid():
        my_new_todo = Todo(todotext=request.POST['text'])
        my_new_todo.save()

    return redirect('index')

def completeTodo(request, todo_id):
    mytodo = Todo.objects.get(pk=todo_id)
    mytodo.complete = True
    mytodo.save()

    return redirect('index')

def deleteTodo(request):
    Todo.objects.filter(complete__exact=True).delete()
    return redirect('index')
