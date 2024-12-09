# from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .models import Student, Result
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

def index(request):
    return render(request, 'results/index.html')


def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        email = request.POST['email']
        student_id = request.POST['student_id']

        user = User.objects.create_user(username=username, email=email, password=password)
        Student.objects.create(user=user, student_id=student_id)
        return redirect('login')
    return render(request, 'results/register.html')


def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('dashboard')
        else:
            return render(request, 'results/login.html', {'error': 'Invalid credentials'})
    return render(request, 'results/login.html')


def user_logout(request):
    logout(request)
    return redirect('index')


def dashboard(request):
    if not request.user.is_authenticated:
        return redirect('login')

    student = Student.objects.get(user=request.user)
    results = Result.objects.filter(student=student)
    return render(request, 'results/dashboard.html', {'results': results})


from django.shortcuts import render, redirect
from .models import Student, Result
from django.contrib.auth.decorators import login_required


@login_required
def dashboard(request):
    if request.method == 'POST':
        student = Student.objects.get(user=request.user)
        courses = request.POST.getlist('course[]')
        marks = request.POST.getlist('marks[]')

        for course, mark in zip(courses, marks):
            Result.objects.create(student=student, course=course, marks=int(mark))

        return redirect('dashboard')

    student = Student.objects.get(user=request.user)
    results = Result.objects.filter(student=student)
    return render(request, 'results/dashboard.html', {'results': results})


def add_results(request):
    return render(request, 'add_results.html')


from django.shortcuts import render


def view_results(request):
    # Sample data to test rendering
    results = [
        {'student_name': 'John Doe', 'course': 'Mathematics', 'marks': 85},
        {'student_name': 'Jane Smith', 'course': 'Science', 'marks': 92},
    ]
    return render(request, 'view_results.html', {'results': results})


from django.shortcuts import render, get_object_or_404
from .models import Result

def result_details(request, id):
    # Fetch the specific result by ID
    result = get_object_or_404(Result, id=id)
    return render(request, 'results/result_details.html', {'result': result})
