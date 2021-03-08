from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from accounts.forms import CreateUserForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout




def registerPage(request):
    form = CreateUserForm()
    context = {'form': form}
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            password = form.cleaned_data['password2']
            password
            # messages.success(request, 'Account created for' + user )
            user = authenticate(username=username, password=password)
            login(request, user)
            # return redirect('index')
            print("helooooo"*50)
            return redirect('login')
    else:
        form = CreateUserForm()
        context = {'form': form}
    return render(request, 'edlyne_times/index.html', context)


def loginPage(request):

    form = CreateUserForm()
    context = {'form': form}
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            print("heloooooooooooooooooooo")
            login(request, user)
            return redirect('index')
        else:
            print("inside ;lslslsllslslslslslsllsls")
            messages.error(request, 'Username or Password Incorrect')
            return render(request, 'accounts/login.html', context)
    else:
        return render(request, 'accounts/login.html', context)


def logoutUser(request):

    logout(request)
    return redirect('index')