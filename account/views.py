from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages, auth
from django.contrib.auth.models import User
from contact.models import Contact


def register(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']

        # Check if passwords match
        if password == password2:
            # check username
            if User.objects.filter(username=username).exists():
                messages.error(request, 'Username already exists')
                return redirect('register')
            else:
                if User.objects.filter(email=email).exists():
                    messages.error(request, 'That email already exists')
                    return redirect('register')
                else:
                    user = User.objects.create_user(username=username,
                    password=password, email=email, first_name=first_name,
                    last_name=last_name)
                    #Login after register
                    auth.login(request, user)
                    messages.success(request, 'You are now logged in')
                    return redirect('index')
        else:
            messages.error(request, 'Passwords do not match')
            return redirect('register')
    else:
        return render(request, 'account/register.html')


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            messages.success(request, 'You have logged in')
            return redirect('dashboard')
        else:
            messages.error(request, 'Invalid login credentials')
            return redirect('login')
    else:
        return render(request, 'account/login.html')


def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        messages.success(request, 'You are logged out')
        return redirect('index')


def dashboard(request):
    user_contact = Contact.objects.order_by('-contact_date').filter(user_id=request.user.id)
    context = {
        'user_contact': user_contact
    }
    return render(request, 'account/dashboard.html', context)


def delete_button(request, id):
    delete = get_object_or_404(Contact, pk=id)
    context = {
        'delete': delete
    }

    if request.method == 'GET':
        delete.delete()
        messages.success(request, 'You have deleted your query')
        return render(request, 'account/dashboard.html', context)
