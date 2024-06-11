from django.shortcuts import render
from django.http import HttpResponse
from .models import Contact
# Create your views here.
def index(request):
    return render(request,"index.html")

def send(request):
    if request.method == 'POST':
        fname=request.POST.get('fname')
        email=request.POST.get('email')
        msg=request.POST.get('msg')
        link=request.POST.get('link')
        sub=request.POST.get('sub')
        c = Contact(fname=fname, email=email, msg=msg, link=link, sub=sub)
        c.save()
        
        
    return render(request, 'index.html')
