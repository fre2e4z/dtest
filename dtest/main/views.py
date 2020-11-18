from django.shortcuts import render


# Create your views here.
def index(request):
    data = {
        'title': 'Главная страница!',
        'values': ['Some', 'hello', '123'],
        'dict': {'name': 'John',
                 'age': '22',
                 'hobby': 'football'
                 }
    }
    return render(request, 'main/index.html', data)

def about(request):
    return render(request, 'main/about.html')