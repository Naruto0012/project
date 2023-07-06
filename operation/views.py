from django.shortcuts import render
from .models import StudentModel
from django.contrib import messages
from .forms import StudentForm

# Create your views here.
def home(request):
    show=StudentModel.objects.all()
    return render(request,'operation/homeAll.html',{'data':show})

def insert(request):
    if request.method=='POST':
        if request.POST.get('Name') and request.POST.get('Course'):
            saverecord=StudentModel()
            saverecord.Name=request.POST.get('Name')
            saverecord.Course=request.POST.get('Course')
            saverecord.save()
            messages.success(request,"Data inserted succesfully")
            return render(request,'operation/insert.html')
    else:
        return render(request,'operation/insert.html')
    

def edit(request,id):
    obj=StudentModel.objects.get(id=id)
    return render(request,'operation/edit.html',{'Obj':obj})
  
def update(request,id):
    Updated=StudentModel.objects.get(id=id)
    forms=StudentForm(request.POST,instance=Updated)
    if forms.is_valid():
        forms.save()
        messages.success(request,"Record Updated Sucessfully")
        
        return render(request,'operation/edit.html',{'Obj':Updated})          
    
def delete(request,id):
    dele=StudentModel.objects.get(id=id)
    dele.delete()
    showdata=StudentModel.objects.all()
    return render(request,'operation/homeAll.html',{'data':showdata})