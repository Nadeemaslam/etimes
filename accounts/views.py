from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from accounts.forms import CreateUserForm
from accounts.forms import ContactForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.core.mail import EmailMessage
from django.shortcuts import redirect
from django.template.loader import get_template


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
            messages.success(request, 'Account created for' + username )
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('login')
        else:
            messages.error(request, form.errors)
            # form = CreateUserForm()
            # context = {'form': form}
    return render(request, 'accounts/register.html', context)


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
    return redirect('index')



def contact(request):
    form_class = ContactForm

    # new logic!
    if request.method == 'POST':
        form = form_class(data=request.POST)

        if form.is_valid():
            contact_name = request.POST.get(
                'contact_name'
                , '')
            contact_email = request.POST.get(
                'contact_email'
                , '')
            form_content = request.POST.get('content', '')

            # Email the profile with the
            # contact information
            template = get_template('accounts/contact_template.txt')
        context = {
            'contact_name': contact_name,
            'contact_email': contact_email,
            'form_content': form_content,
        }
        content = template.render(context)

        email = EmailMessage(
            "New contact form submission",
            content,
            "ETIMES MEDIA" + '',
            ['er.nadeemaslam89@gmail.com'],
            headers={'Reply-To': contact_email}
        )
        email.send()
        return redirect('accounts/contact')

    return render(request, 'accounts/contact.html', {
        'form': form_class,
    })