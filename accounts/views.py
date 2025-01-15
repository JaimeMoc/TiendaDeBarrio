from django.shortcuts import render
from django.contrib.auth.forms import AuthenticationForm

def login_view(request):
    
    if request.method == "POST":
        pass
    
    form = AuthenticationForm()
    return render(request, 'accounts/login.html', {'form': form})