from django.shortcuts import render

# Create your views here.
def info(request):
    return render(request, 'info.html')
def student(request, name):
    return render(request, 'student.html', {'name':name})
    
def throw(request):
    return render(request, 'throw.html')
    
def catch(request):
    message = request.GET.get('message')
    return render(request, 'catch.html', {'message': message})