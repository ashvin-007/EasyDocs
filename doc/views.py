from django.shortcuts import render,redirect
from .models import *
from django.http import FileResponse
import os
from django.conf import settings
from django.shortcuts import get_object_or_404
from .forms import *
from django.contrib.auth.models import User
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages

# Create your views here.

def home(request):
    document=DocUpload.objects.all()
    if request.GET.get('search'):
        search=request.GET.get('search')
        document=document.filter(title__icontains=search)
        if not document.exists():
            document=[]
    # user=UserRegisterForm()
    
    return render(request,'home.html',{'document':document})
@login_required(login_url='loggedin')
def download_pdf(request, document_id):
    document = get_object_or_404(DocUpload, id=document_id)
    file_path = os.path.join(settings.MEDIA_ROOT, document.doc.name)

    return FileResponse(open(file_path, 'rb'), as_attachment=True, content_type='application/pdf')
@login_required(login_url='loggedin')
def addDoc(request):
    if request.method == 'POST':
        form = docUploadForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Document Uploaded Successfully')  # Message is stored
            return redirect('home')  # Redirect to home
    else:
        form = docUploadForm()

    return render(request, 'add_doc.html', {'form': form})

            
        
            
    

    
def register(request):
    if request.method=='POST':
        form=UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()  
            login(request, user)  
            messages.success(request,'Account Crerated Successsfully')
            return redirect('home')   
    else:
        form=UserRegisterForm(request.POST)
        return render(request,'register.html',{'form':form})
    
    return render(request,'register.html',{'form':form})    





def loggedin(request):
     

    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)  
            if user is not None:
                login(request, user)
                messages.success(request,'Login Successsfully')
                return redirect('home')
    form = AuthenticationForm() 
    return render(request, 'login.html', {'form': form})


def loggedout(request):
    logout(request)
    messages.success(request,'You Are Logout')
    return redirect('home')
    