from django.shortcuts import render
from django.http import JsonResponse
from .models import Student

# Create your views here.

def home(request):
    return render(request, 'home.html')

def create_student(request):
    name = request.POST['name']
    age = request.POST['age']
    mail = request.POST['mail']

    student = Student.objects.create(
        name=name,
        age=age,
        email=mail
    )
    return JsonResponse({
        "success": True,
        "message": "Data added successfully"
    })
