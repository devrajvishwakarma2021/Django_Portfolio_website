from django.shortcuts import redirect, render
from django.contrib import messages
from portfolio.models import Contact,Blog,Internship
# Create your views here.
def home(request):
    return render(request, 'basic.html')
    # return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def internship(request):
    if not request.user.is_authenticated:
        messages.warning(request,'Please login to access this page')
        return redirect("/auth/login/")
    
    if request.method =='POST':
        fname=request.POST.get('name')
        femail=request.POST.get('email')
        fusn=request.POST.get('usn')
        fcollege=request.POST.get('collegename')
        foffer=request.POST.get('offer')
        fstartdate=request.POST.get('startdate')
        fenddate=request.POST.get('enddate')
        fprojectreport=request.POST.get('projectreport')

        

        fname=fname.upper()
        fusn=fusn.upper()
        fcollege=fcollege.upper()
        fprojectreport=fprojectreport.upper()
        foffer=foffer.upper()
        
        check1 = Internship.objects.filter(usn=fusn)
        check2 = Internship.objects.filter(email=femail)

        if check1 or check2 :
               messages.warning(request,'Your Details are Stored Already')
               return redirect('/intershipdetails')




        query=Internship(fullname=fname, usn=fusn, email=femail, college_name=fcollege, offer_status=foffer, 
                          start_date=fstartdate, end_date=fenddate, proj_report=fprojectreport)
        
        query.save()
        messages.success(request,'Form is Submitted Success')
        return redirect('/intershipdetails')

    return render(request, 'intern.html')

    
def blog(request):
    posts=Blog.objects.all()
    context={"posts":posts}
    return render(request, 'blog.html',context)

def contact(request):
    if request.method =='POST':
        fname=request.POST.get('name')
        femail=request.POST.get('email')
        fphone=request.POST.get('number')
        fdesc=request.POST.get('desc')
        query=Contact(name=fname, email=femail,  phonenumber=fphone, desc=fdesc)
        query.save()
        messages.success(request, 'Thankyou for contating us. we will  get by you Soon! ')
        return redirect('/contact')
    return render(request, 'contact.html')