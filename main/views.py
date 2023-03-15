from django.shortcuts import render, reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from .models import *
from .forms import *
from django.http import Http404

from rest_framework.decorators import api_view
from rest_framework.response import Response
from main.serializers import PostSerializer

def index(request):
	# Get the profile of logged in user
	if request.user.is_authenticated:
		profile = Profile.objects.get_or_create(user=request.user)[0]

	posts = Post.objects.all()


	images = ImageModel.objects.all()

	if request.method == 'GET':

	####    Get the search properties from frontend	
		searched = request.GET.get('searched')
		city = request.GET.get('city')

		minM = request.GET.get('minM')
		maxM = request.GET.get('maxM')

		minMoney = request.GET.get('min$')
		maxMoney = request.GET.get('max$')

		propertyType = request.GET.get('property')
		offertType = request.GET.get('offert')
	####
		

	####  Filter by every search variables
		if searched:
			posts = posts.filter(title=searched)

		if city:
			posts = posts.filter(city=city)

		if minM:
			posts = posts.filter(meters__gte=minM)

		if maxM:
			posts = posts.filter(meters__lte=maxM)

		if minMoney:
			posts = posts.filter(price__gte=minMoney)

		if maxMoney:
			posts = posts.filter(price__lte=maxMoney)
			

		if propertyType:
			if propertyType != "None":
				posts = posts.filter(PropertyType=propertyType)

		if offertType:
			if offertType != "None":
				posts = posts.filter(OffertType=offertType)
	####
	

	context = {"posts": posts,"images":images}

	return render(request, 'main/index.html', context)

@login_required
def new(request):
	if request.user.is_authenticated:
		profile = Profile.objects.get_or_create(
	user=request.user)[0]
	
	if request.method == 'POST':
		form = PostForm(request.POST)
		imageForm = ImageForm(request.POST, request.FILES)

		if form.is_valid() and imageForm.is_valid():

			formForImage = form.save(commit=False)
			imageForm.save(commit=False)

			form.instance.author = profile
			imageForm.instance.post = formForImage
			

			form.save()
			imageForm.save()

			form = PostForm(request.POST)
			imageForm = ImageForm(request.POST, request.FILES)
	
			return HttpResponseRedirect(reverse('main:profile', kwargs={'profileID':request.user.username}))
	else:
		form = PostForm(request.POST)
		imageForm = ImageForm(request.POST)

	context = {'form' : form, 'imageForm' : imageForm}
	return render(request, 'main/new.html', context)

@login_required
def profile(request, profileID):
	
	# Try to get the desired profile, raise 404 if it doesnt exist
	try:
		profile = Profile.objects.get_or_create(
	user=profileID)[0]
	except Profile.DoesNotExist:
		raise Http404

	posts = Post.objects.filter(
	author=profile)
	
	images = ImageModel.objects.all()

	context = {"profile":profile,"posts":posts,"images":images}

	return render(request, 'main/profile.html', context)

@login_required
def edit(request):

	profile = Profile.objects.get_or_create(
	user=request.user)[0]


	if request.method == 'POST':
		form = ProfileEditForm(request.POST, instance=profile)
		

		if form.is_valid():


			form.save()
			return HttpResponseRedirect(reverse('main:profile', kwargs={'profileID':request.user.username}))
	else:
		form = ProfileEditForm(instance=profile)
	return render(request, 'main/edit.html', {'form' : form})

def editpost(request, postID):

	post = Post.objects.get_or_create(
	id=postID)[0]


	if request.method == 'POST':
		form = PostEditForm(request.POST, instance=post)
		

		if form.is_valid():


			form.save()
			return HttpResponseRedirect(reverse('main:profile', kwargs={'profileID':request.user.username}))
	else:
		form = PostEditForm(instance=post)
	return render(request, 'main/editpost.html', {'form' : form})

def deletepost(request, postID):

	post = Post.objects.filter(id=postID).delete()
	

	return HttpResponseRedirect(reverse('main:profile', kwargs={'profileID':request.user.username}))


def post(request, postID):
	

	post = Post.objects.get_or_create(
	id=postID)[0]
	image = ImageModel.objects.filter(
	post=post)[0]

	context = {"post":post,"image":image}

	return render(request, 'main/post.html', context)	

##### API for Serializers

@api_view(['GET'])
def post_collection(request):
	if request.method == 'GET':
		posts = Post.objects.all()
		serializer = PostSerializer(posts, many=True)
		return Response(serializer.data)


@api_view(['GET'])
def post_element(request, pk):
	try:
		post = Post.objects.get(pk=pk)
	except Post.DoesNotExist:
		return HttpResponse(status=404)

	if request.method == 'GET':
		serializer = PostSerializer(post)
		return Response(serializer.data)

@api_view(['POST'])
def AddPostAPI(request):
	if request.method == 'POST':
		posts = Post.objects.all()
		serializer = PostSerializer(data=request.data)

		if serializer.is_valid():
			serializer.save()
		return Response()
#########		