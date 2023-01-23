from django.shortcuts import render
from .forms import *
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required



def get_register(request):

    if request.method == 'POST':
        form = AdminForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Signup successfully")
            return redirect('login')
    else:
        form = AdminForm()
    return render(request, "pages/register.html", {"form": form})


def get_login(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, "login successfully")
                return redirect("/")
        else:
            messages.success(request, "Invalid login or password.")    
    else:
        
        form = AuthenticationForm()
      

    return render(request, "pages/login.html", {"form": form})




        

def get_logout(request):
    logout(request)
    messages.success(request, "Logout successfully")

    return redirect("login")

@login_required(login_url='login')
def createuser(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "User create successfully")
            return redirect("/")

    else:
        form = UserForm()
    return render(request,"pages/create_user.html",{"form": form})    



@login_required(login_url='login')
def get_userlist(request):
    enquires=Artist.objects.order_by('create_at')
    context={
        'enquires':enquires,
    }    
    return render(request,'pages/index.html',context)


@login_required(login_url='login')
def user_update(request, pk):

    if request.method == "POST":
        data = Artist.objects.get(id=pk)
        form = UserForm(request.POST,  instance=data)
        if form.is_valid():
            form.save()
            messages.success(request, "User update successfully")
            return redirect("/")
    else:
        data = Artist.objects.get(id=pk)
        form = UserForm( instance=data)

    context = {
        "data": data,
        "form": form,
    }
 
    return render(request, "pages/userupdate.html", context)

@login_required(login_url='login')
def user_delete(request, pk):
    data = Artist.objects.get(id=pk)
    data.delete()
    messages.success(request, "user delete successfully")
    return redirect("/")


@login_required(login_url='login')
def createartist(request):
    if request.method == 'POST':
        form = ArtistForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Artist create successfully")
            return redirect("artist-list")

    else:
        form = ArtistForm()
    return render(request,"pages/create_artist.html",{"form": form})    



@login_required(login_url='login')
def get_artistlist(request):
    enquires=Music.objects.all()
    context={
        'enquires':enquires,
    }    
    return render(request,'pages/list_artist.html',context)


@login_required(login_url='login')
def artist_update(request, pk):

    if request.method == "POST":
        data = Music.objects.get(id=pk)
        form = ArtistUpdateForm(request.POST,  instance=data)
        if form.is_valid():
            form.save()
            messages.success(request, "Artist update successfully")
            return redirect("artist-list")
    else:
        data = Music.objects.get(id=pk)
        form = ArtistUpdateForm( instance=data)

    context = {
        "data": data,
        "form": form,
    }
 
    return render(request, "pages/artistupdate.html", context)

@login_required(login_url='login')
def delete_artist(request, pk):
    data = Music.objects.get(id=pk)
    data.delete()
    messages.success(request, "Artist delete successfully")
    return redirect("artist-list")