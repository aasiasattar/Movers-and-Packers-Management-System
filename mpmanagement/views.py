import imp
from itertools import count
from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login, logout

from .models import *
from datetime import date
from django.db.models import Q

# Create your views here.

def index(request):
    return render(request,'index.html')


def admin_login(request):
    error = ""
    if request.method =='POST':
        u = request.POST['username']
        p = request.POST['pwd']
        user = authenticate(username=u,password=p)
        if user.is_staff:
            login(request,user)
            error = "no"
        else:
            error = "yes"

    return render(request,'admin_login.html',locals())


def admin_home(request):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    totalservices = Services.objects.all().count()
    totalnewmsgs = Contact.objects.filter(is_read="no").count()
    totaloldmsgs = Contact.objects.filter(is_read="yes").count()
    totalnewbookings = SiteUser.objects.filter(status=None).count()
    totaloldbookings = SiteUser.objects.filter(status="old booking").count()
    
   

    return render(request,'admin_home.html',locals())


def Logout(request):
    logout(request)

    return redirect('index')


def add_services(request):
    error = ""
    if not request.user.is_authenticated:
        return redirect('admin_login')

    if request.method=='POST':
        s = request.POST['servicetitle']
        d = request.POST['description']
        i = request.FILES['image']
        
        try:
           Services.objects.create(title=s,description=d,image=i)
           error = "no"

        except:
            error = "yes"
        

    return render(request,'add_services.html',locals())
    


def manage_services(request):
    error = ""
    if not request.user.is_authenticated:
        return redirect('admin_login')

    services = Services.objects.all()

    return render(request,'manage_services.html',locals())



def edit_service(request,pid):
   
    if not request.user.is_authenticated:
        return redirect('admin_login')
    service = Services.objects.get(id=pid)
    error = ""
    if request.method=='POST':
        s = request.POST['servicetitle']
        d = request.POST['description']
        

        service.title = s
        service.description = d
        
        try:
            service.save()
            error = "no"

        except:
              error = "yes"

        try:
            i = request.FILES['image']
            service.image = i
            service.save()
        except:
             pass

    return render(request,'edit_service.html',locals())



def delete_service(request,pid):
    service = Services.objects.get(id=pid)
    service.delete()
    return redirect('manage_services')




def services(request):
    
    services = Services.objects.all()

    return render(request,'services.html',{'services':services})

    

def about(request):
    
     return render(request,'about.html')


def request_form(request):
    error = ""
    if request.method=='POST':
        n = request.POST['name']
        e = request.POST['email']
        c = request.POST['contact']
        l = request.POST['location']
        sl = request.POST['shiftinglocation']
        bi = request.POST['briefitems']
        i = request.POST['items']
        sd = request.POST['shiftingdate']
        
        try:
           SiteUser.objects.create(name=n,email=e,mobile=c,location=l,shifting_loc=sl,brief_items=bi,items=i,shiftingdate=sd,requestdate=date.today())
           error = "no"

        except:
            error = "yes"
        

    return render(request,'request_form.html',locals())




def new_booking(request):
   
    if not request.user.is_authenticated:
        return redirect('admin_login')

    booking = SiteUser.objects.filter(status=None)
    return render(request,'new_booking.html',locals())



def old_booking(request):
    
    if not request.user.is_authenticated:
        return redirect('admin_login')

    booking = SiteUser.objects.filter(status="old booking")
    return render(request,'old_booking.html',locals())



def view_bookingdetail(request,pid):
    error = ""
    if not request.user.is_authenticated:
        return redirect('admin_login')
    booking = SiteUser.objects.get(id=pid)
    if request.method == 'POST':
        remark = request.POST['remark']

        try:
            booking.remark = remark
            booking.status = "old booking"
            booking.updationdate = date.today()
            booking.save()
            error = "no"

        except:
            error = "yes"
        
    return render(request,'view_bookingdetail.html',locals())




def delete_booking(request,pid):
    booking = SiteUser.objects.get(id=pid)
    booking.delete()
    return redirect('old_booking')


def contact(request):
    error = ""
    if request.method=='POST':
        fn = request.POST['fullname']
        c = request.POST['contact']
        e = request.POST['email']
        s = request.POST['subject']
        msg = request.POST['message']
        try:
            Contact.objects.create(name=fn,number=c,email=e,subject=s,message=msg,msg_date=date.today(),is_read="no")
            error = "no"
        except:
            error = "yes"
    return render(request,'contact.html',locals())





def new_messages(request):
   
    if not request.user.is_authenticated:
        return redirect('admin_login')
    messages = Contact.objects.filter(is_read="no")
    
    return render(request,'new_messages.html',locals())



def old_messages(request):
    
    if not request.user.is_authenticated:
        return redirect('admin_login')

    messages = Contact.objects.filter(is_read="yes")
    
    return render(request,'old_messages.html',locals())



def view_messagesdetail(request,pid):
   
    if not request.user.is_authenticated:
        return redirect('admin_login')
    messages = Contact.objects.get(id=pid)
    messages.is_read = "yes"
    messages.save()
        
    return render(request,'view_messagesdetail.html',locals())



def delete_message(request,pid):
    message = Contact.objects.get(id=pid)
    message.delete()
    return redirect('old_messages')


def search(request):
    
    if request.method=='POST':
        sd = request.POST['searchdata']
    try:
        booking = SiteUser.objects.filter(Q(name=sd)|Q(mobile=sd))
    except:
         booking =  ""

    return render(request,'search.html',locals())



def bookingreport_betweendates(request):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    
    if request.method=='POST':
        fd = request.POST['fromdate']
        td = request.POST['todate']
        booking = SiteUser.objects.filter(Q(requestdate__gte=fd) & Q(requestdate__lte=td))
        return render(request,'bookingbetween_dates.html',locals())
   

    return render(request,'bookingreport_betweendates.html',locals())



def msgsform_betweendates(request):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    
    if request.method=='POST':
        fd = request.POST['fromdate']
        td = request.POST['todate']
        messages = Contact.objects.filter(Q(msg_date__gte=fd) & Q(msg_date__lte=td))
        return render(request,'msgsshow_betweendates.html',locals())
   

    return render(request,'msgsform_betweendates.html',locals())





def change_password(request):
    if not request.user.is_authenticated:
        return redirect('admin_login')

    error = ""
    
    if request.method=="POST":
        c = request.POST['currentpassword']
        n = request.POST['newpassword']
       
        try:
            u = User.objects.get(id=request.user.id)
            if u.check_password(c):
               u.set_password(n)
               u.save()
               error = "no"
            else:
                error = "not"
                
        except:
            error = "yes"

    
    
    return render(request,'change_password.html',locals())

    







    

