

from django.urls import path,include
from .import views

urlpatterns = [

    path('login/',views.loginView,name='login_page_link'),
    path('logout/',views.logoutView,name='logout_link')
]
