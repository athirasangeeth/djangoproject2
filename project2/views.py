from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def samplefunction(request):
 return HttpResponse("school")
def loginfunction(request):
    return render(request,'login.html')
def signupfunction(request):
        return render(request,'signup.html')