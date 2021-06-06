from django.shortcuts import render

from django.contrib.auth.forms import UserCreationForm
from .models import AuctionItem
from .forms import ProductCreateFrom,biddingForm

# Create your views here.
def homeView(request):
   return render(request, 'product_bid.html')


def myDashboardView(request):
   items = AuctionItem.objects.all()

   return render(request,'my_Dashboard.html',{'data':items})


def cateogryView(request,cats_name):
   return render(request,'product_category_view.html',{"category":cats_name})



def test_theme(request):
   return render(request,'test_theme.html',{})


def auctiongalleryView(request):
   data = AuctionItem.objects.all()

   return render(request,'action_glellary.html',{"data":data})





