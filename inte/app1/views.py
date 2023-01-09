from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import CustomUser, Details, uploaded_files
from .forms import booksForm
import datetime

# Create your views here.


@login_required()
def HomePage(request):
    return render(request, 'index.html')


def RegisterPage(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        uname = request.POST.get('username')
        pass1 = request.POST.get('password1')
        pass2 = request.POST.get('password2')
        fname = request.POST.get('fullname')
        city = request.POST.get('city')
        loca = request.POST.get('location')
        dob = request.POST.get('birth_date')
        p_v = request.POST.get('pub_vis')
        print(uname, email, pass1, pass2, fname, city)

        if pass1 != pass2:
            return HttpResponse("Passwords do not match")
        else:
            my_user = CustomUser.objects.create_user(uname, email, pass1)
            my_user.save()

            d_user = Details(uname=uname, email=email, fullname=fname, city=city, public_visibility=p_v, birth_date=dob, location=loca)
            d_user.save()
            messages.success("User Created Successfully")
            return redirect('login')

    return render(request, 'register.html')


def LoginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        pass1 = request.POST.get('pass')
        print(username, pass1)
        user = authenticate(request, username=username, password=pass1)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            return HttpResponse("Incorrect password or username!!!")

    return render(request, 'login.html')


def LogoutPage(request):
    logout(request)
    return redirect('login')


def ForgotpasswordPage(request):
    return render(request, 'forgot-password.html')

def Authors_SellersPage(request):
    user_list = Details.objects.order_by('-public_visibility')
    if request.method == "POST":
        vis = request.POST.get('vis')
        print(vis)
        if vis == 1:
            user_list = Details.objects.filter(public_visibility="1")
            print(user_list)
        elif vis == 2:
            user_list = Details.objects.filter(public_visibility="0")
            print(user_list)

    return render(request, 'Authors_Sellers.html', {'user_list': user_list})

def Upload_BooksPage(request):
    if request.method == "POST":
        form = booksForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
        messages.success(request, ("Form submitted successfully"))
        return redirect('uploaded_books')

    form = booksForm
    return render(request, 'Upload_Books.html', {'form': form})

def Uploaded_BooksPage(request):
    books_list = uploaded_files.objects.order_by('Year')
    print(books_list)
    return render(request, 'Uploaded_books.html', {'books_list': books_list})

def MyBooksPage(request):
    books_list = uploaded_files.objects.order_by('Year')
    print(books_list)
    return render(request, 'My_books.html', {'books_list': books_list})
