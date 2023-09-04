"""blogsite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path
from blogapp import views
from django.conf.urls.static import static
from django.conf import settings
from django.urls import include
from blogapp.views import *
from blogapp.views import CommentView



urlpatterns = [
    path('admin/', admin.site.urls),
    path('create', views.create,name='create'),
    path('',views.read,name='home'),
    path('update/<int:id>',views.update,name='update'),
    path('delete/<int:id>',views.delete,name='delete'),
    path('search',views.search,name='search'),
    path('page1',views.first,name='first'),
    path('category',views.Categories,name='category'),
    path('CategoryBlog<str:tag>' , views.CategoryBlog , name='CategoryBlog'),
    path('CurrentUserProfile',views.CurrentUserProfile , name='CurrentUserProfile'),
    path('CurrentUserProfileUpdate',views.CurrentUserProfileUpdate , name='CurrentUserProfileUpdate'),
    path('UserDataupdate' , views.UserDataupdate,name='UserDataupdate'),
    path('likes<int:id>' , views.Likes , name='likes'),
    path('Comment<int:id>/',CommentView.as_view(), name='Comment'),  
    path("Comment/Update/<int:id>", views.CommentUpdateview, name="CommentUpdate"),
    path("Comment/Delete/<int:id>", views.CommentDeleteview, name="CommentDelete"),
    path("ContactView", views.ContactView, name="ContactView"),
    path('Download/<int:id>' , views.DownloadPdf , name='DownloadPdf'),
    
    

    path('',include('AuthApp.urls')),
    

   


]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
