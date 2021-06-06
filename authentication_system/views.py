from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.contrib import messages


# Create your views here.
from django.contrib.auth import authenticate,login,logout

def loginView(request):
   if request.method =="POST":
      print("post accpected")
      username = request.POST['username']
      password = request.POST['password']
      # print(username)
      # print(password)
      user = authenticate(request, username=username, password=password)
      if user is not None:
         login(request, user)
         messages.success(request,"logged in success fully")
         return redirect('auction_gallery_link')
      else:
         messages.success(request,"{} this user is not register".format(username))
         return redirect('login_page_link')

   else:
      return render(request,'login.html')


def logoutView(request):
   logout(request)
   messages.success(request,("log out successfully"))
   return redirect('auction_gallery_link')
      # Redirect to a success page.




