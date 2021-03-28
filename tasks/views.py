from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import *
from .forms import *
def index(request):
    if request.method == "POST":
        form=TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = TaskForm()
    tasks=Task.objects.all()
    contex={'tasks':tasks,'form':form}
    return render(request,'tasks/list.html',contex)
def updateTask(request,pk):
    task = Task.objects.get(pk=pk)
    if request.method == "POST":
        form=TaskForm(request.POST,instance=task)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
         form = TaskForm(instance=task)
    context={'form':form}
    return render(request,'tasks/update_task.html',context)
def deleteTask(request,pk):
    item=Task.objects.get(id=pk)
    if request.method=='POST':
        item.delete()
        return redirect('/')
    context={'item':item}
    return render(request,'tasks/delete_task.html',context)
