from django.shortcuts import render,redirect
from BackendApp.models import EventCategoryDB,SubeventDb,MovieDB,SportsDB,DetailsDb,Bookingdb,admindb,contactdb
from django.utils.datastructures import MultiValueDictKeyError
from django.core.files.storage import FileSystemStorage
from django.contrib.auth import authenticate,login
from django.contrib.auth.models import User
from django.contrib import messages


# Create your views here.

def indexpage(request):
    return render(request,"index.html")




def registration(request):
    return render(request,"useregister.html")

def adminregister(request):
    if request.method=="POST":
        na=request.POST.get('name')
        em=request.POST.get('email')
        pa=request.POST.get('password')

        obj=admindb(Name=na,Email=em,Password=pa)
        obj.save()
        return redirect(registration)

def adminlogin(request):
    if request.method == "POST":
        username_r = request.POST.get('username')
        password_r = request.POST.get('password')
        if User.objects.filter(username__contains=username_r).exists():
            user = authenticate(username=username_r, password=password_r)
            if user is not None:
                login(request, user)
                request.session['username'] = username_r
                request.session['password'] = password_r
                return redirect(indexpage)
            else:
                return redirect(registration)
        else:
            return redirect(registration)

def adminlogout(request):
    del request.session['username']
    del request.session['password']
    return redirect(registration)


def EventCategory(request):
    return render(request,"Event_Category.html")

def savecategory(request):
    if request.method=="POST":
        na=request.POST.get('name')
        de=request.POST.get('description')
        im=request.FILES['image']
        obj=EventCategoryDB(Name=na,Description=de,Image=im)
        obj.save()
        messages.success(request,"Category added succesfully")
        return redirect(EventCategory)

def displaycategory(request):
    categorydata=EventCategoryDB.objects.all()
    return render(request,"Display_Event_category.html",{"categorydata":categorydata})

def  editcategory(req,dataid):
    editcategorydata=EventCategoryDB.objects.get(id=dataid)
    return render(req,"Edit_Event_Category.html",{"editcategorydata":editcategorydata})

def updatecategory(req,dataid):
    if req.method == "POST":
        na = req.POST.get('name')
        de = req.POST.get('description')
        try:
            img=req.FILES['image']
            fs=FileSystemStorage()
            file=fs.save(img.name,img)
        except MultiValueDictKeyError:
            file=EventCategoryDB.objects.get(id=dataid).Image
        EventCategoryDB.objects.filter(id=dataid).update(Name=na,Description=de,Image=file)
        messages.success(req, "Category updated succesfully")
        return redirect(displaycategory)

def deletecategory(req,dataid):
    deletecategorydata=EventCategoryDB.objects.filter(id=dataid)
    deletecategorydata.delete()
    messages.warning(req, "Category Removed")
    return redirect(displaycategory)

def SubCategory(request):
    catdata=EventCategoryDB.objects.all()
    return render(request,"Add_SubCategory.html",{"catdata":catdata})

def savesubcategory(request):
    if request.method=="POST":
        ca=request.POST.get('category')
        na=request.POST.get('subname')
        de=request.POST.get('subdescription')
        im=request.FILES['subeventimage']
        obj=SubeventDb(Category_Name=ca,Subcategory_name=na,Sub_description=de,Sub_Image=im)
        obj.save()
        messages.success(request, "SubCategory added succesfully")
        return redirect(SubCategory)

def displaysubcategory(request):
    subcategorydata=SubeventDb.objects.all()
    return render(request,"Display_SubCategory.html",{"subcategorydata":subcategorydata})

def  editsubcategory(req,dataid):
    editsubcategorydata=SubeventDb.objects.get(id=dataid)
    catda=EventCategoryDB.objects.all()
    return render(req,"Edit_SubCategory.html",{"editsubcategorydata":editsubcategorydata,"catda":catda})

def updatesubcategory(req,dataid):
    if req.method == "POST":
        ca = req.POST.get('category')
        na = req.POST.get('subname')
        de = req.POST.get('subdescription')
        try:
            img=req.FILES['subeventimage']
            fs=FileSystemStorage()
            file=fs.save(img.name,img)
        except MultiValueDictKeyError:
            file=SubeventDb.objects.get(id=dataid).Sub_Image
        SubeventDb.objects.filter(id=dataid).update(Category_Name=ca,Subcategory_name=na,Sub_description=de,Sub_Image=file)
        messages.success(req, "SubCategory updated succesfully")
        return redirect(displaysubcategory)

def deletesubcategory(req,dataid):
    deletesubcategorydata=SubeventDb.objects.filter(id=dataid)
    deletesubcategorydata.delete()
    messages.warning(req, "SubCategory Removed")
    return redirect(displaysubcategory)

def Movie(request):
    catgdata=EventCategoryDB.objects.filter(Name="Movies")
    subdata=SubeventDb.objects.all()
    return render(request,"Add_Movie.html",{"catgdata":catgdata,"subdata":subdata})

def savemovie(request):
    if request.method=="POST":
        ca=request.POST.get('category')
        sc=request.POST.get('subcategory')
        na=request.POST.get('moviename')
        de=request.POST.get('moviedescription')
        cs=request.POST.get('moviecast')
        rt=request.POST.get('movietime')
        ms=request.POST.get('moviescreen')
        st=request.POST.get('showtime')
        im=request.FILES['movieimage']
        obj=MovieDB(Category_name=ca,Subcategory_Name=sc,Movie_Name=na,Movie_Description=de,Movie_Cast=cs,Movie_Time=rt,Movie_Screen=ms,Show_Time=st,Movie_Image=im)
        obj.save()
        messages.success(request, "Movie added succesfully")
        return redirect(Movie)

def displaymalayalam(request):
    eventdata=MovieDB.objects.filter(Subcategory_Name="Malayalam Movies")
    return render(request,"Display_Malayalam.html",{"eventdata":eventdata})

def displaytamil(request):
    eventdata=MovieDB.objects.filter(Subcategory_Name="Tamil Movies")
    return render(request,"Display_Tamil.html",{"eventdata":eventdata})

def displayenglish(request):
    eventdata=MovieDB.objects.filter(Subcategory_Name="English Movies")
    return render(request,"Display_English.html",{"eventdata":eventdata})

def  editmovie(req,dataid):
    moviedata=MovieDB.objects.get(id=dataid)
    catgda=EventCategoryDB.objects.all()
    subcatdata=SubeventDb.objects.all()
    return render(req,"Edit_Movie.html",{"moviedata":moviedata,"catgda":catgda,"subcatdata":subcatdata})

def updatemovie(request,dataid):
    if request.method == "POST":
        ca = request.POST.get('category')
        sc = request.POST.get('subcategory')
        na = request.POST.get('moviename')
        de = request.POST.get('moviedescription')
        cs = request.POST.get('moviecast')
        rt = request.POST.get('movietime')
        ms = request.POST.get('moviescreen')
        st = request.POST.get('showtime')
        try:
            img=request.FILES['movieimage']
            fs=FileSystemStorage()
            file=fs.save(img.name,img)
        except MultiValueDictKeyError:
            file=MovieDB.objects.get(id=dataid).Movie_Image
        MovieDB.objects.filter(id=dataid).update(Category_name=ca,Subcategory_Name=sc,Movie_Name=na,Movie_Description=de,Movie_Cast=cs,Movie_Time=rt,Movie_Screen=ms,Show_Time=st,Movie_Image=file)
        messages.success(request, "Movie info updated succesfully")
        return redirect(Movie)

def deletemovie(req,dataid):
    deletemoviedata=MovieDB.objects.filter(id=dataid)
    deletemoviedata.delete()
    messages.warning(req, "Movie Removed")
    return redirect(displaysubcategory)


def Sports(request):
    catg_data=EventCategoryDB.objects.filter(Name="Sports")
    sub_data=SubeventDb.objects.all()
    return render(request,"Add_Match.html",{"catg_data":catg_data,"sub_data":sub_data})

def savesports(request):
    if request.method=="POST":
        ca=request.POST.get('category')
        sc=request.POST.get('subcategory')
        mi=request.POST.get('matchinfo')
        mv=request.POST.get('matchvenue')
        md=request.POST.get('matchdate')
        mt=request.POST.get('matchtime')
        ig=request.FILES['matchimage']
        obj=SportsDB(Category_name=ca,Subcategory_Name=sc,Match_Info=mi,Match_Venue=mv,Match_Date=md,Match_Time=mt,Match_Image=ig)
        obj.save()
        messages.success(request, "Match added succesfully")
        return redirect(Sports)


def displayCricket(request):
    event_data=SportsDB.objects.filter(Subcategory_Name="Cricket")
    return render(request,"Display_Cricket.html",{"event_data":event_data})

def displayFootball(request):
    event_data=SportsDB.objects.filter(Subcategory_Name="Football")
    return render(request,"Display_Football.html",{"event_data":event_data})

def  editsports(req,dataid):
    sportsdata=SportsDB.objects.get(id=dataid)
    catg_da=EventCategoryDB.objects.all()
    subcat_data=SubeventDb.objects.all()
    return render(req,"Edit_Sports.html",{"sportsdata":sportsdata,"catg_da":catg_da,"subcat_data":subcat_data})

def updatesports(request,dataid):
    if request.method == "POST":
        ca = request.POST.get('category')
        sc = request.POST.get('subcategory')
        mi = request.POST.get('matchinfo')
        mv = request.POST.get('matchvenue')
        md = request.POST.get('matchdate')
        mt = request.POST.get('matchtime')
        try:
            img=request.FILES['matchimage']
            fs=FileSystemStorage()
            file=fs.save(img.name,img)
        except MultiValueDictKeyError:
            file=SportsDB.objects.get(id=dataid).Match_Image
        SportsDB.objects.filter(id=dataid).update(Category_name=ca,Subcategory_Name=sc,Match_Info=mi,Match_Venue=mv,Match_Date=md,Match_Time=mt,Match_Image=file)
        messages.success(request, "Match info updated succesfully")
        return redirect(Sports)

def deletesports(req,dataid):
    deletesportsdata=SportsDB.objects.filter(id=dataid)
    deletesportsdata.delete()
    messages.warning(req, "Match Removed")
    return redirect(displaysubcategory)

def displaycustomer(req):
    user_data=DetailsDb.objects.all()
    return render(req,"Display_users.html",{"user_data":user_data})

def displaybooking(req):
    book_data=Bookingdb.objects.all()
    return render(req,"Display_booking.html",{"book_data":book_data})

def displaymessage(req):
    message_data = contactdb.objects.all()
    return render(req,"display_message.html",{"message_data":message_data})