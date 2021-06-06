
from django.views.generic import DeleteView,ListView,DetailView,CreateView,UpdateView
from .models import AuctionItem,Bidding_auction
from .forms import ProductCreateFrom,ProductUpdateForm,biddingForm
from django.urls import reverse_lazy
from django.db.models import Avg, Max, Min, Sum



class createPorductView(CreateView):
   model = AuctionItem
   template_name = "create_Auction_item.html"
   #fields = '__all__' #use for select all the field
   #fields = ('title','body') #selected field
   form_class = ProductCreateFrom


class editProductView(UpdateView):
   model = AuctionItem
   template_name = 'update_auction_item.html'
   form_class = ProductUpdateForm

class singleProductView(DetailView):
   model = AuctionItem
   template_name = 'product_profile.html'




   def get_context_data(self, *args, **kwargs):
      bidding_auction = Bidding_auction.objects.all()

      #max_value = Bidding_auction.objects.aggregate(m)

      context = super(singleProductView, self).get_context_data(*args, **kwargs)


      context['bidding_auction']=bidding_auction
      #context['max_bid_price'] =max_value


      return context







class deleteProductView(DeleteView):
   model = AuctionItem
   template_name = 'delete_product.html'
   success_url = reverse_lazy('auction_gallery_link')

class BiddingView(CreateView):
   model = Bidding_auction
   form_class = biddingForm
   template_name = 'post_bid.html'


   def form_valid(self, form):
      form.instance.bdding_item_id = self.kwargs['pk']
      print(self.kwargs['pk'])
      return super().form_valid(form)

   def get_success_url(self):
      return reverse_lazy('singe_product_view_link', kwargs={'pk': self.kwargs['pk']})

   # success_url = reverse_lazy('auction_gallery_link')




# class BiddingView(CreateView):
#    model = Bidding_auction
#    template_name = 'product_profile.html'
#    fields = '__all__'

