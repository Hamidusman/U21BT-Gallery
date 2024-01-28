from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'index.html')

def students(request):
    return render(request, 'students.html')