from django.shortcuts import render
from .models import Info
def index(request):
    if request.method == 'POST':
        email=request.POST['email']
        number=request.POST['number']
        message=request.POST['message']
        info = Info(email=email,number=number,message=message)
        info.save()

    return render(request,('index.html'))
