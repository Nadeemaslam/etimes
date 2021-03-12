from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from accounts.forms import CreateUserForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout




def registerPage(request):
    form = CreateUserForm()
    context = {'form': form}
    print("111111111")
    if request.method == 'POST':
        print("22222222")
        form = CreateUserForm(request.POST)
        # print(regForm.errors)
        print(form.errors,"peppepep")
        if form.is_valid():
            print('333333333')
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            password = form.cleaned_data['password2']
            password
            messages.success(request, 'Account created for' + username )
            user = authenticate(username=username, password=password)
            login(request, user)
            # return redirect('index')
            print("helooooo"*50)
            return redirect('login')
        else:
            print("44444444ggggjgjj")
            messages.error(request, form.errors)
            # form = CreateUserForm()
            # context = {'form': form}
        print("5555555")
    return render(request, 'accounts/register.html', context)


def loginPage(request):

    form = CreateUserForm()
    context = {'form': form}
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password1')
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


