"""inte URL Configuration

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
from app1 import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.RegisterPage, name='register'),
    path('login/', views.LoginPage, name='login'),
    path('home/', views.HomePage, name='home'),
    path('logout/', views.LogoutPage, name='logout'),
    path('forgot-password/', views.ForgotpasswordPage, name='forgot-password'),
    path('auth_sel/', views.Authors_SellersPage, name='auth_sel'),
    path('upload_books/', views.Upload_BooksPage, name='up_books'),
    path('uploaded_books/', views.Uploaded_BooksPage, name='uploaded_books'),
    path('my_books/', views.MyBooksPage, name='my_books')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
