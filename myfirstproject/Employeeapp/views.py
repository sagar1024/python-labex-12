from django.shortcuts import render
from django.http import HttpResponse

def hi(request):
    return render(request, 'Employeeapp/home.html')

