from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from accounts.forms import CreateUserForm
from accounts.forms import ContactForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.core.mail import send_mail
from django.shortcuts import redirect
from .decorators import allowed_users, user_authenticated

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
            messages.success(request, 'Account created for ' + username )
            return redirect('login')
        else:
            messages.error(request, form.errors)
            # form = CreateUserForm()
            # context = {'form': form}
    return render(request, 'accounts/register.html', context)

@user_authenticated
def loginPage(request):

    form = CreateUserForm()
    context = {'form': form}
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password1')
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            messages.error(request, 'Username or Password Incorrect')
            return render(request, 'accounts/login.html', context)
    else:
        return render(request, 'accounts/login.html', context)


def logoutUser(request):

    logout(request)
    return redirect('login')



def contact(request):
    form_class = ContactForm

    # new logic!
    if request.method == 'POST':
        form = form_class(request.POST)

        if form.is_valid():
            contact_name = form.cleaned_data['contact_name']
            sender = form.cleaned_data['contact_email']
            comment = form.cleaned_data['comment']
            msg_mail = str(comment) + " " + str(sender)
            recipients = ['edlynetimesmedia@gmail.com']
            send_mail(contact_name,comment,sender,recipients, fail_silently=True)
            return render(request,'accounts/contact.html', {'message':contact_name})
        return redirect('accounts/contact')

    return render(request, 'accounts/contact.html', {
        'form': form_class,
    })