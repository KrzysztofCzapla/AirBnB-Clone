from django.urls import path
from django.conf.urls import url
from . import views
from django.conf.urls import include
from django.conf import settings
from django.conf.urls.static import static
app_name = 'main'
urlpatterns = [
    path('', views.index, name='main'),
    path('profile/<profileID>/', views.profile, name='profile'),
    path('post/<postID>/', views.post, name='post'),
    path('edit/', views.edit, name = 'edit'),
    path('new/', views.new, name = 'new'),
    path('editpost/<postID>/', views.editpost, name = 'editpost'),
    path('deletepost/<postID>/', views.deletepost, name = 'deletepost'),
    # api stuff
    path('api/posts/', views.post_collection, name = 'post_collection'),
    path('api/post/<postID>/', views.post_element, name = 'post_element'),
    path('api/posts/add/', views.AddPostAPI, name = 'AddPostAPI'), 
]

if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,
                              document_root=settings.MEDIA_ROOT)
        urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)