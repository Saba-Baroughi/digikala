from django.shortcuts import render, redirect
from .models import Product
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

def helloworld(request):
    all_products=Product.objects.all()
 
    return render(request, 'index.html', {'products': all_products})

def about(request):
    return render(request, 'about.html')

def login_user(request):
    # if request.method=="POST" bud means: yani az tarige url cizi barayam ersal nashode bud, bia va karhaye login ra anjam bede
    if request.method == "POST": 
        username=request.POST['username']
        password=request.POST['password']

        user=authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request,("Successfully Loged in!"))
            return redirect("home")
        else:
            messages.success(request,("Your username or password is incorrect! "))
            return redirect("login")    
    else:    
        return render(request, 'login.html')


def logout_user(request):
    logout(request)
    messages.success(request, ('Successfully log out!'))
    return redirect("home")

