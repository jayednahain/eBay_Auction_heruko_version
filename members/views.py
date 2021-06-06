from django.shortcuts import render,redirect
from .forms import SingUpForm,UpdateUserForm,changePasswordForm
from django.contrib.auth import authenticate,login
from django.contrib import messages
from django.contrib.auth.forms import PasswordChangeForm
from shop_app.models import AuctionItem





# Create your views here.


def profileView(request):
   items = AuctionItem.objects.all()

   return render(request,'user_profile.html',{"items":items})


def userRegistration(request):
   form = SingUpForm(request.POST)
   if request.method == "POST":
      if form.is_valid():
         form.save()
         username = form.cleaned_data['username']
         password = form.cleaned_data['password1']
         user = authenticate(username=username,password=password)
         login(request,user)
         messages.success(request,("register successfully"))
         return redirect('home_link')

   else:
      form=SingUpForm()
   data = {
      "form":form
   }
   return render(request,'user_registation.html',data)


def updateUserdataView(request):
   form = UpdateUserForm(request.POST,instance=request.user)
   if request.method == "POST":
      if form.is_valid():
         form.save()
         messages.success(request, ("information Update Successfully"))
         return redirect('profile_link')

   else:
      form = UpdateUserForm(instance=request.user)
   data = {
      "form": form
   }
   return render(request,'user_profile_update.html',data)

def changeUserPasswordVeiw(request):
   form = changePasswordForm(data=request.POST, user=request.user)
   if request.method == "POST":
      if form.is_valid():
         form.save()
         messages.success(request, ("information Update Successfully"))
         return redirect('profile_link')

   else:
      form = changePasswordForm(user=request.user)
   data = {
      "form": form
   }

   return render(request,'user_password_update.html',data)