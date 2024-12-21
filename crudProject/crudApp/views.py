from django.shortcuts import render, redirect
from .models import Stduent
from django.contrib import messages
from django.db.models import Q
from django.template.loader import render_to_string
from datetime import datetime

from django.core.mail import send_mail

# Create your views here.
def home(request):
    data=Stduent.objects.filter(IsDelete=False)
    

    return render(request, 'crudApp/home.html',{'infodata':data})

date=datetime.now()
def form(request):
    if request.method == 'POST':
        nm=request.POST['name']
        age=request.POST['age']
        email=request.POST['email']
        phone_number=request.POST['Phone_number']
        
        
        Stduent.objects.create(name=nm, age=age, email=email, phone_number=phone_number)
        subject="Python Training"
        message=render_to_string('crudApp/msg.html',{'name': nm,'date':date})
        from_email="chadaniale123@gmail.com"
        recipient_list=[email]

        send_mail(subject,message,from_email, recipient_list,fail_silently=False)





        messages.success(request, f"Hello {nm}, your form is successfully register!!!")
        return redirect('form')
    return render(request, 'crudApp/form.html')

def contact(request):
    return render(request, 'crudApp/contact.html')

def about(request):
    return render(request, 'crudApp/about.html')

def delete_data(request,id):
    stu=Stduent.objects.get(id=id)
    stu.IsDelete=True
    stu.save()
    messages.success(request, "Successfully Deleted")
    return redirect('home')

def edit(request,id): 
    if request.method == 'POST':
        data=Stduent.objects.get(id=id)

      
        data.name=request.POST['name']
        data.age=request.POST['age']
        data.email=request.POST['email']
        data.phone_number=request.POST['Phone_number']
        data.save()

        messages.success(request, "your form is successfully updated!!! " )
        return redirect('home')
    else:
        data=Stduent.objects.get(id=id)


    return render(request, 'crudApp/edit.html', {'data': data})



def search_form(request):
    if request.method=='POST':
        searched=request.POST['searched']
        find=Stduent.objects.filter(Q(name__icontains=searched)|Q(age__icontains=searched))

        # find1=Stduent.objects.filter(name__icontains=searched)
        # find2=Stduent.objects.filter(age__icontains=searched)
        # find=find1.union(find2)
    else:
        messages.info(request, "Data is not found.")
    return render(request, 'crudApp/search.html', {'finds': find})