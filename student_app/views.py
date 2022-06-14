from django.shortcuts import render,HttpResponse,redirect
from student_app.forms import studentform,facultyform
from student_app.models import studentdetail,facultydetail
# Create your views here.

def home(request):
    #code write here for home page
    return render(request,'home.html',{})

def add(request):
    if(request.method=='POST'):
        form=studentform(request.POST)
        if(form.is_valid()):
            form.save()
            return redirect('/admin')
        else:
            return render(request,"register.html",{'form':form})
    else:
        form=studentform()
        return render(request,"register.html",{'form':form})

def add_f(request):
    if(request.method=='POST'):
        form=facultyform(request.POST)
        if(form.is_valid()):
            form.save()
            return redirect('/admin')
        else:
            return render(request,"f_register.html",{'form':form})
    else:
        form=facultyform()
        return render(request,"f_register.html",{'form':form})

def show(request):
    data=studentdetail.objects.all()
    data2=facultydetail.objects.all()
    return render(request,"details.html",{'student':data,'faculty':data2})

def update(request,id):
    obj=studentdetail.objects.get(roll_number=id)
    form=studentform(request.POST or None,instance=obj)
    if(request.method=='POST'):
        if(form.is_valid()):
            form.save()
            return redirect('/student_app/search')
    return render(request,"register.html",{'form':form})

def delete(request,id):
    obj=studentdetail.objects.get(roll_number=id)
    obj.delete()
    return redirect ("/student_app/search")

