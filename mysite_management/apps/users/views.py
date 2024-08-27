from django.shortcuts import render, redirect
from django.contrib.auth.hashers import make_password
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from apps.users.models import User
from .forms import UserAddForm, UserForm
from django.contrib import messages
# Create your views here.

@login_required(login_url='login')
def index(request):
    DB = User.objects.filter(user_role_id=2).order_by('-id')
    totalRecord = DB.count()
    paginator = Paginator(DB, 2)  
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'page_obj':page_obj,
        'totalRecord': totalRecord,
        'users_obj': DB,
    }
    return render(request, 'users/index.html', context)

@login_required(login_url='login')
def add(request):
    if request.method == 'POST':
        form = UserAddForm(request.POST or None)
        if form.is_valid():
            users = User()
            users.user_role_id = 2
            users.username = form.cleaned_data["username"]
            users.first_name =form.cleaned_data["first_name"]
            users.last_name = form.cleaned_data["last_name"]
            users.email = form.cleaned_data["email"]
            users.mobile_number = form.cleaned_data["mobile_number"]
            users.password = make_password(form.cleaned_data["password"])
            users.confirm_password = make_password(form.cleaned_data["confirm_password"])
            users.is_staff = True
            users.save()

            return redirect("users")

    else:
        form = UserAddForm()
    context = {
        "form": form,
    }
    return render(request, 'users/add.html', context)

@login_required(login_url='login')
def edit(request, id):
    user = User.objects.get(id=id)
    if not user:
        return redirect('index')
    initialDict = {
        "email": user.email,
        "username": user.username,
        "first_name": user.first_name,
        "last_name": user.last_name,
        "mobile_number": user.mobile_number
    }
    form = UserForm(initial=initialDict)
    if request.method == "POST":
        form = UserForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            messages.success(request, "you are now logged in")
            return redirect('users')

    context = {
        'form': form,
        'user_data': user,
    }
    return render(request, 'users/edit.html', context)


@login_required(login_url='login')
def delete(request, id):
    user = User.objects.get(id=id)
    if not user:
        return redirect('index')
    user.is_delete = True
    user.is_active = False
    user.email = user.email + '_deleted_' + str(id)
    user.username = user.username + '_deleted_' + str(id)
    user.delete()
    # user.save()
    return redirect('users')
