from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.


class AuctionItem(models.Model):
   product_name = models.CharField(max_length=255)
   #headr_images = models.ImageField(null=True,blank=True,upload_to="images/")
   product_description =models.TextField(max_length=400)
   product_main_price = models.IntegerField(default=0.0)
   current_bid_price = models.IntegerField(default=0.0)

   author =models.ForeignKey(User,on_delete=models.CASCADE)

   main_photo = models.ImageField(null=True,blank=True,upload_to='photos/main/%Y/%m/%d/')
   photo1 = models.ImageField(null=True,blank=True,upload_to='photos/optional/%Y/%m/%d/')
   photo2 = models.ImageField(null=True,blank=True,upload_to='photos/optional/%Y/%m/%d/')
   photo3 = models.ImageField(null=True,blank=True,upload_to='photos/optional/%Y/%m/%d/')
   photo4 = models.ImageField(null=True,blank=True,upload_to='photos/optional/%Y/%m/%d/')

   item_post_date =models.DateField(auto_now_add=True)



   auction_start_time = models.DateTimeField(auto_now=False,null=True)

   acution_end_time = models.DateTimeField(auto_now=False,null=True)



   category = models.CharField(max_length=255,default="uncatpegorized")


   #snippet = models.CharField(max_length=255, default="")
   #likes = models.ManyToManyField(User,related_name='blog_posts')

   def __str__(self):
      return str(self.product_name)+ ' | ' + str(self.author)

   def get_absolute_url(self):
      return reverse('my_dashboard_link')


class Category(models.Model):
   name = models.CharField(max_length=105)

   def __str__(self):
      return self.name

   def get_absolute_url(self):
      return reverse('home_link')


class Bidding_auction(models.Model):
   bdding_author_name = models.CharField(max_length=100)


   bdding_item = models.ForeignKey(AuctionItem,related_name='biddings', on_delete=models.CASCADE)

   #body
   Biggin_Price = models.IntegerField(default=0.0)

   bidding_date = models.DateField(auto_now_add=True)


   def __str__(self):
      return str(self.bdding_author_name) +"|"+str(self.bdding_item)






