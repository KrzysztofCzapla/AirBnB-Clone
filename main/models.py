from django.db import models
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify

class Profile(models.Model):
	user = models.OneToOneField(User, default=User, on_delete=models.CASCADE)
	name = models.CharField(max_length=20, default="User")	
	#profile_img = models.ImageField(upload_to='images/',default='/images/basic.png')
	bio = models.CharField(max_length=50,default="No Description")
	phoneNumber = models.CharField(max_length=15,default="Not Added")
	eMail = models.CharField(max_length=50,default="Not Added")
	
class Post(models.Model):
	author = models.ForeignKey(Profile,default=Profile,null=True, on_delete=models.CASCADE,related_name='author')

	OffertTypes = [
		('Buy','Buy'),
		('Rent','Rent'),
	]
	OffertType = models.CharField(
		max_length=4,
		choices=OffertTypes,
		default='Rent',
	)


	PropertyTypes = [
		('House','House'),
		('Apartment','Apartment'),
	]
	PropertyType = models.CharField(
		max_length=9,
		choices=PropertyTypes,
		default='House',
	)

	title = models.CharField(max_length=100)
	Description = models.CharField(max_length=5000)
	date = models.DateTimeField("Published: ",auto_now=True)
	price = models.DecimalField(max_digits=15, decimal_places=0,default=0)
	meters = models.DecimalField(max_digits=15, decimal_places=0,default=0)
	city = models.CharField(max_length=50,default=None)

class ImageModel(models.Model):
	image = models.ImageField(upload_to='images/',
                              verbose_name='Image',default=None)

	post = models.ForeignKey(Post,default=Post,null=True, on_delete=models.CASCADE,related_name='post')
	

	
	
	

	

