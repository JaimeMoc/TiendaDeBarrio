from django.shortcuts import render

def login_view(request):
    
    if request.method == "POST":
        pass
        
    return render(request, 'accounts/login.html')