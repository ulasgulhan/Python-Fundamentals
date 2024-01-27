from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import CreateUserForm, LoginForm, UpdateUserForm


# Create your views here.

def register(request):
    form = CreateUserForm()

    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.save()
            return redirect('my_login')

    context = {
        'form': form
    }

    return render(request, 'register.html', context)


def my_login(request):
    form = LoginForm()

    if request.method == 'POST':
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('dashboard')

    context = {
        'form': form
    }

    return render(request, 'my-login.html', context)


# def user_logout(request):
#     try:
#         for key in list(request.session.key()):
#             if key == 'session_key':
#                 continue
#             else:
#                 del request.session[key]
#     except KeyError:
#         pass
#
#     messages.success(request, 'Logout has been success')
#     return redirect('store')


def user_logout(request):
    logout(request)
    messages.success(request, 'Logout has been success')
    return redirect('store')


@login_required(login_url='my_login')
def profile_management(request):
    user_form = UpdateUserForm(instance=request.user)

    if request.method == 'POST':
        user_form = UpdateUserForm(request.POST, instance=request.user)

        if user_form.is_valid():
            user_form.save()

            messages.info(request, 'Update has been successes')

            return redirect('dashboard')

    context = {
        'user_form': user_form
    }

    return render(request, 'profile-management.html', context)


@login_required(login_url='my_login')
def delete_account(request):
    user = User.objects.get(id=request.user.id)

    if request.method == 'POST':
        user.delete()

        messages.error(request, 'Account has been deleted')

        return redirect('store')

    return render(request, 'delete-account.html')


@login_required(login_url='my_login')
def dashboard(request):
    return render(request, 'dashboard.html')
