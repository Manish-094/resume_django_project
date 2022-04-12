from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def services(request):
    context = {'service':'active'}
    return render(request,'services/services.html',context)
    
