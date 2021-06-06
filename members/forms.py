from django.contrib.auth.models import User
from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm,PasswordChangeForm



class SingUpForm(UserCreationForm):


   '''first_name = forms.CharField(max_length=100)
   last_name = forms.CharField(max_length=100)'''

   email = forms.EmailField(widget=forms.EmailInput(attrs={
      'class': 'form-control',
      'placeholder':"Email"
   }),label='')
   first_name = forms.CharField(max_length=100,widget=forms.TextInput(attrs={
      'class': 'form-control',
      'placeholder':"Frist Name"
   }),label='')
   last_name = forms.CharField(max_length=100,widget=forms.TextInput(attrs={
      'class':'form-control',
      'placeholder':"Last Name"
   }),label='')


   class Meta:
      model = User
      fields = ('username','first_name','last_name','email','password1','password2')


   #for appling username and password we need to define another methods

   def __init__(self,*args,**kwargs):
      super(SingUpForm,self).__init__(*args,**kwargs)

      classes={
         'class':'form-control'
      }

      self.fields['username'].widget.attrs['class'] = 'form-control'
      self.fields['username'].widget.attrs['placeholder'] = 'Username'
      self.fields['username'].label=""
      self.fields['username'].help_text ="<span class='form-text text-muted'><small>Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.</small></span>"

      self.fields['password1'].widget.attrs['class'] = 'form-control'
      self.fields['password1'].widget.attrs['placeholder'] = 'Password'
      self.fields['password1'].label = ""
      self.fields['password1'].help_text="<ul class='form-text text-muted small'><li>Your password can’t be too similar to your other personal information.</li><li>Your password must contain at least 8 characters.</li><li>Your password can’t be a commonly used password.</li><li>Your password can’t be entirely numeric.</li></ul>"

      self.fields['password2'].widget.attrs['class'] = 'form-control'
      self.fields['password2'].widget.attrs['placehol der'] = 'Confirm Password'
      self.fields['password2'].label = ""
      self.fields['password2'].help_text ="<span class='form-text text-muted'><small>Enter the same password as before, for verification.</small></span>"



      # select_fields = ['username','password1','password2']
      #
      # for value in select_fields:
      #    self.fields[value].widget.attrs['class'] = 'form-control'
      #    self.fields[value].widget.attrs['placeholder'] = str(value)



class UpdateUserForm(UserChangeForm):


   email = forms.EmailField(widget=forms.EmailInput(attrs={
      'class': 'form-control',
      'placeholder': "Email"
   }), label='')
   first_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={
      'class': 'form-control',
      'placeholder': "Frist Name"
   }), label='')
   last_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={
      'class': 'form-control',
      'placeholder': "Last Name"
   }), label='')
   class Meta:
      model = User
      fields = ('username','first_name','last_name','email')


   def __init__(self,*args,**kwargs):
      super(UpdateUserForm,self).__init__(*args,**kwargs)

      self.fields['username'].widget.attrs['class'] = 'form-control'
      self.fields['username'].widget.attrs['placeholder'] = 'Username'
      self.fields['username'].label = ""
      self.fields['username'].help_text = "<span class='form-text text-muted'><small>Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.</small></span>"


class changePasswordForm(PasswordChangeForm):
   class Meta:
      model = User
      fields = ('old_password','new_password1','new_password2')









