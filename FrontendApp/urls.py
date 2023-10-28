from FrontendApp import views
from django.urls import path

urlpatterns=[
 path('home_page/', views.home_page, name="home_page"),
 path('errorpage/', views.errorpage, name="errorpage"),
 path('seat/<det>', views.seat, name="seat"),
 path('seatconfirm/', views.seatconfirm, name="seatconfirm"),
 path('details/', views.details, name="details"),
 path('saveuserdetails/', views.saveuserdetails, name="saveuserdetails"),
 path('ticket/', views.ticket, name="ticket"),
 path('deleteticket/<int:dataid>', views.deleteticket, name="deleteticket"),
 path('payment/', views.payment, name="payment"),
 path('contactus/', views.contactus, name="contactus"),
 path('savemessage/', views.savemessage, name="savemessage"),
 path('aboutus/', views.aboutus, name="aboutus"),













 path('category/', views.category, name="category"),
 path('movie_sep/<catg>', views.movie_sep, name="movie_sep"),
 path('movie_one/', views.movie_one, name="movie_one"),
 path('sports_one/', views.sports_one, name="sports_one"),
 path('detailed/<det>', views.detailed, name="detailed"),


 path('signin/', views.signin, name="signin"),
 path('user_reg/', views.user_reg, name="user_reg"),
 path('userlogin/', views.userlogin, name="userlogin"),
 path('logout/', views.logout, name="logout"),
 path('edituser/', views.edituser, name="edituser"),
 path('updateuser/', views.updateuser, name="updateuser"),









 ]