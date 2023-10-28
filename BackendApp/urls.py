from BackendApp import views
from django.urls import path

urlpatterns=[
    path('indexpage/', views.indexpage, name="indexpage"),

    path('adminlogin/', views.adminlogin, name="adminlogin"),
    path('adminlogout/', views.adminlogout, name="adminlogout"),
    path('adminregister/', views.adminregister, name="adminregister"),
    path('registration/', views.registration, name="registration"),




    path('EventCategory/', views.EventCategory, name="EventCategory"),
    path('savecategory/', views.savecategory, name="savecategory"),
    path('displaycategory/', views.displaycategory, name="displaycategory"),
    path('editcategory/<int:dataid>', views.editcategory, name="editcategory"),
    path('updatecategory/<int:dataid>', views.updatecategory, name="updatecategory"),
    path('deletecategory/<int:dataid>', views.deletecategory, name="deletecategory"),

    path('SubCategory/', views.SubCategory, name="SubCategory"),
    path('savesubcategory', views.savesubcategory, name="savesubcategory"),
    path('displaysubcategory', views.displaysubcategory, name="displaysubcategory"),
    path('editsubcategory/<int:dataid>', views.editsubcategory, name="editsubcategory"),
    path('updatesubcategory/<int:dataid>', views.updatesubcategory, name="updatesubcategory"),
    path('deletesubcategory/<int:dataid>', views.deletesubcategory, name="deletesubcategory"),

    path('Movie/',views.Movie,name="Movie"),
    path('savemovie/',views.savemovie,name="savemovie"),
    path('displaymalayalm/',views.displaymalayalam,name="displaymalayalam"),
    path('displaytamil/',views.displaytamil,name="displaytamil"),
    path('displayenglish/',views.displayenglish,name="displayenglish"),
    path('editmovie/<int:dataid>', views.editmovie, name="editmovie"),
    path('updatemovie/<int:dataid>', views.updatemovie, name="updatemovie"),
    path('deletemovie/<int:dataid>', views.deletemovie, name="deletemovie"),

    path('Sports/', views.Sports, name="Sports"),
    path('savesports/', views.savesports, name="savesports"),
    path('displayCricket/', views.displayCricket, name="displayCricket"),
    path('displayFootball/', views.displayFootball, name="displayFootball"),
    path('editsports/<int:dataid>', views.editsports, name="editsports"),
    path('updatesports/<int:dataid>', views.updatesports, name="updatesports"),
    path('deletesports/<int:dataid>', views.deletesports, name="deletesports"),

    path('displaycustomer/',views.displaycustomer,name="displaycustomer"),
    path('displaybooking/',views.displaybooking,name="displaybooking"),
    path('displaymessage/',views.displaymessage,name="displaymessage"),



]