
from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

# Create your views here.
def signup(request):
    if request.method=='POST':
        get_email=request.POST.get('email')
        get_pass=request.POST.get('pass1')
        get_conf=request.POST.get('pass2')

        if get_pass != get_conf:
            messages.info(request, 'Password is not matching')
            return redirect('/auth/signup')
        
        try:
            if User.objects.get(username=get_email):
                messages.warning(request, "Email is Taken")
                return redirect('/auth/signup')
        except Exception as identifier:
            pass

        myuser=User.objects.create_user(get_email, get_email, get_pass)
        myuser.save()
        myuser= authenticate(username=get_email, password=get_pass)
        if myuser is not None:
            login(request,myuser)
            messages.success(request,'User Create & Login Success')
        # messages.success(request, 'User is Created Please Login')
        return redirect('/')
                
    return render(request, 'signup.html')


def handlelogin(request):
    if request.method=='POST':
        get_email=request.POST.get('email')
        get_pass=request.POST.get('pass1')
        myuser= authenticate(username=get_email, password=get_pass)

        if myuser is not None:
            login(request,myuser)
            messages.success(request,'Login Success')
        else:
            messages.error('Invalid credentials')
    return render(request, 'login.html')

def handlelogout(request):
    logout(request)
    messages.success(request,'Logout Success')
    return render(request, 'logout.html')

