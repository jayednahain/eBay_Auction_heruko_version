
from django.urls import path
from .import views

urlpatterns = [

   path('profile',views.profileView, name='profile_link'),
   path('user_registration',views.userRegistration,name='user_registration_link'),
   path('user_profile_update',views.updateUserdataView,name='update_profile_link'),
   path('user_passowrd_update',views.changeUserPasswordVeiw,name='passowrd_change_link')


]
