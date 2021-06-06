from django.contrib import admin
from .models import AuctionItem,Category,Bidding_auction

# Register your models here.


admin.site.register(AuctionItem)
admin.site.register(Category)
admin.site.register(Bidding_auction)


