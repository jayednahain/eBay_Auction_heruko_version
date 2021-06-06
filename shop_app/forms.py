from shop_app.models import AuctionItem,Category,Bidding_auction

from django import forms


choices=Category.objects.all().values_list('name','name')

choices_list = []

for items in choices:
   choices_list.append(items)


class ProductCreateFrom(forms.ModelForm):

   class Meta:
      model = AuctionItem
      #fields = ('title','title_page','author','category','body','snippet','headr_images')
      fields=['product_name','main_photo','photo1','photo2','photo3','photo4','category','product_description','auction_start_time','acution_end_time','product_main_price','author']

      widgets = {
         'product_name': forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': "Product Name"
         }),
         'category': forms.Select(choices=choices_list,attrs={
            'class': 'form-control',


         }),
         'product_description': forms.Textarea(attrs={
            'class': 'form-control',
            'placeholder':'Describe'
         }),

         'auction_start_time':forms.DateTimeInput(attrs={
            'class': 'form-control',
            'type': 'date'

         }),

         'acution_end_time':forms.DateTimeInput(attrs={
            'class': 'form-control',
            'type': 'date'

         }),




         'product_main_price': forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Describe'
         }),
         'current_bid_price': forms.TextInput(attrs={
            'class': 'form-control',



         }),
         'author': forms.Select(attrs={
            'class': 'form-control'
         }),
      }


      #make all the labels property null
      # labels = {}
      # keys = range(len(fields))
      # for i in fields:
      #    labels[i] = ""





class ProductUpdateForm(forms.ModelForm):

   class Meta:
      model = AuctionItem
      #fields = ('title','title_page','author','category','body','snippet','headr_images')
      fields=['product_name','main_photo','photo1','photo2','photo3','photo4','category','auction_start_time','acution_end_time','product_description','product_main_price']

      widgets = {
         'product_name': forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': "Product Name"
         }),
         'category': forms.Select(choices=choices_list,attrs={
            'class': 'form-control',


         }),
         'product_description': forms.Textarea(attrs={
            'class': 'form-control',
            'placeholder':'Describe'
         }),
         # 'author':forms.Select(attrs=author_style),

         'auction_start_time': forms.DateTimeInput(attrs={
            'class': 'form-control',
            'type': 'date'

         }),

         'acution_end_time': forms.DateTimeInput(attrs={
            'class': 'form-control',
            'type': 'date'

         }),



         'product_main_price': forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Describe'
         }),
         'current_bid_price': forms.TextInput(attrs={
            'class': 'form-control',
         }),

      }


class biddingForm(forms.ModelForm):
   class Meta:
      model = Bidding_auction
      fields = ['bdding_author_name','Biggin_Price']


      widgets = {
         'bdding_author_name':forms.TextInput(attrs={
            'class': 'form-control',
            'type':'hidden'
         }),
         'Biggin_Price':forms.NumberInput(attrs={
            'class': 'form-control',
            'placeholder': "Product Name"
         }),

      }


