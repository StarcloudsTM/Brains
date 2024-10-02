# views.py
from django.shortcuts import render

def home(request):
    return render(request, 'home.html', {'message': 'Hello from Django!'})

# In templates/home.html:
# <h1>{{ message }}</h1>
