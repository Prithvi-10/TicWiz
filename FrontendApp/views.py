from django.shortcuts import render,redirect
from BackendApp.models import EventCategoryDB,SubeventDb,MovieDB,Bookingdb,DetailsDb,contactdb
from FrontendApp.models import registerdb
from django.contrib.auth import authenticate,login
from django.contrib import messages

# Create your views here.
def home_page(request):
    return render(request,"home.html")

def category(request):
    cat_data = EventCategoryDB.objects.all()
    return render(request,"category.html",{"cat_data":cat_data})

def movie_sep(request,catg):
    sub_data=SubeventDb.objects.filter(Category_Name=catg)
    return render(request,"sub_category.html",{"sub_data":sub_data})

def movie_one(request):
    movdata=SubeventDb.objects.filter(Category_Name="Movies")
    return render(request,"movie_only.html",{"movdata":movdata})

def sports_one(request):
    spodata=SubeventDb.objects.filter(Category_Name="Sports")
    return render(request,"sports_only.html",{"spodata":spodata})

def detailed(request,det):
    det_data=MovieDB.objects.filter(Subcategory_Name=det)
    foot_data = SubeventDb.objects.filter(Category_Name="Sports")
    return render(request,"seperate.html",{"det_data":det_data,"foot_data":foot_data})



def errorpage(request):
    return render(request,"sports_one.html")

def signin(request):
    return render(request,"signup.html")

def user_reg(request):
    if request.method=="POST":
        na=request.POST.get('name')
        em=request.POST.get('email')
        pa=request.POST.get('password1')
        pa2=request.POST.get('password2')
        obj=registerdb(Name=na,Email=em,Password=pa,C_password=pa2)
        obj.save()
        return redirect(signin)

def edituser(request):
    userid=request.session['username1']
    edit_user=registerdb.objects.filter(Name=userid)
    return render(request,"display_signin.html",{"edit_user":edit_user})

def updateuser(request):
    userid=request.session['username1']
    if request.method == "POST":
        na = request.POST.get('name')
        em = request.POST.get('email')
        pa = request.POST.get('password1')
        pa2 = request.POST.get('password2')
        registerdb.objects.filter(Name=userid).update(Name=na,Email=em,Password=pa,C_password=pa2)
        return redirect(home_page)

def userlogin(request):
    if request.method=="POST":
        username_r=request.POST.get('username')
        password_r=request.POST.get('password')
        if registerdb.objects.filter(Name=username_r,Password=password_r).exists():

            request.session['username1'] = username_r
            request.session['password1'] = password_r

            return redirect(home_page)
        else:
            return redirect(signin)
    return redirect(signin)

def logout(request):
    del request.session['username1']
    del request.session['password1']
    return redirect(home_page)

def seat(request,det):
    det_data = MovieDB.objects.filter(Movie_Name=det)
    occupied_seats = Bookingdb.objects.filter(Movie=det).values_list('Seat', flat=True)
    occupied_seats_str = ','.join(occupied_seats)

    return render(request,"seat_booking.html",{"det_data":det_data,'occupied_seats': occupied_seats_str})

def seatconfirm(request):
    
    if request.method=="POST":
        na=request.POST.get('name')
        sc=request.POST.get('seats')
        mo=request.POST.get('movie')
        sn=request.POST.get('screen')
        ti=request.POST.get('time')
        dt = request.POST.get('date')
        pr=request.POST.get('price')
        obj=Bookingdb(Name=na,Seat=sc,Movie=mo,Screen=sn,Time=ti,Date=dt,Price=pr)
        obj.save()
        return redirect(details)

def details(request):
    tkt_data=Bookingdb.objects.filter(Name=request.session['username1'])
    return render(request,"details_entry.html",{"tkt_data":tkt_data})

def saveuserdetails(request):
    if request.method == "POST":
        na = request.POST.get('name')
        mb = request.POST.get('mobile')
        em = request.POST.get('email')

        obj = DetailsDb(Name=na,Mobile=mb,Email=em)
        obj.save()

        return redirect(payment)

def payment(request):

    seat_data = Bookingdb.objects.filter(Name=request.session['username1'])
    return render(request,"payment.html",{"seat_data":seat_data})

def ticket(request):
    seat_data = Bookingdb.objects.filter(Name=request.session['username1'])
    us_data = DetailsDb.objects.filter(Name=request.session['username1'])

    return render(request,"Ticket.html",{"seat_data":seat_data,"us_data":us_data})

def deleteticket(req,dataid):
    deleteticketdata=Bookingdb.objects.filter(id=dataid)
    deleteticketdata.delete()
    messages.error(req, "Ticket Cancelled")
    return redirect(ticket)

def contactus(request):
    return render(request,"contactus.html")

def savemessage(request):
    if request.method=="POST":
        na = request.POST.get('name')
        em = request.POST.get('email')
        sb = request.POST.get('subject')
        ms = request.POST.get('message')

        obj = contactdb(Name=na,Email=em,Subject=sb,Message=ms)
        obj.save()

        return redirect(contactus)

def aboutus(request):
    return render(request,"aboutus.html")





