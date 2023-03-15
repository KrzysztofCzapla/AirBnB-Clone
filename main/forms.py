from django import forms
from django.forms import Textarea
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class ProfileEditForm(forms.ModelForm):

	name = forms.CharField(label='name')
	bio = forms.CharField(label='bio')
	phoneNumber = forms.CharField(label='phoneNumber')
	eMail = forms.CharField(label='eMail')
	class Meta:
		model = Profile
		fields = ['name','bio','phoneNumber','eMail']
		initial=123

class PostEditForm(forms.ModelForm):

	class Meta:
		model = Post
		fields ="__all__"
		exclude = ['author']
		auto_id = False
		widgets = {
            'Description': Textarea(attrs={'cols': 80, 'rows': 20}),
        }


class PostForm(forms.ModelForm): 
	#text = forms.CharField(label='')
	#text.widget.attrs.update({'class': 'text'})


	class Meta:
		model = Post
		fields ="__all__"
		exclude = ['author']
		auto_id = False
		widgets = {
            'Description': Textarea(attrs={'cols': 80, 'rows': 20}),
        }

class ImageForm(forms.ModelForm): 
	#text = forms.CharField(label='')
	#text.widget.attrs.update({'class': 'text'})
	image = forms.ImageField(label='image')

	class Meta:
		model = ImageModel
		fields ="__all__"
		exclude = ['post']
		auto_id = False
