from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from contact.models import Contact
from listings.models import Listing
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin, PermissionRequiredMixin
from django.views.generic import DeleteView, CreateView, UpdateView, ListView
from .forms import StaffListingForm
from .decorators import allowed_users, staff_only


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


@login_required(login_url='login')
@allowed_users(allowed_roles=['user', 'admin', 'staff'])
def dashboard(request):
    user_contact = Contact.objects.order_by('-contact_date').filter(user_id=request.user.id)
    context = {
        'user_contact': user_contact
    }
    return render(request, 'account/dashboard.html', context)


@login_required(login_url='login')
@staff_only
def staffdashboard(request):
    staff_contact = Contact.objects.all().order_by('-contact_date')
    context = {
        'staff_contact': staff_contact
    }
    return render(request, 'account/staffdashboard.html', context)


@login_required(login_url='login')
@allowed_users(allowed_roles=['admin', 'staff'])
def updateListings(request, id):
    listing = Listing.objects.get(id)
    form = StaffListingForm(instance=listing)

    if request.method == 'POST':
        form = StaffListingForm(request.POST, instance=listing)
        if form.is_valid():
            form.save()
            return redirect('/')

    context = {'form': form}
    return render(request, 'account/staffdashboard.html', context)


# class StaffDashboardView(LoginRequiredMixin, UpdateView):
#     template_name = 'staffdashboard.html'
#     success_url = 'staffdashboard'
#     model = Contact
#     form_class = StaffListingForm

#     def form_valid(self, form):
#         form.instance.staff = self.request.user
#         date = form.cleaned_data['contact_date']

#     def test_func(self):
#         """ Test user is staff or throw 403 """
#         if self.request.user.is_staff:
#             return True
#         else:
#             return self.request.user == self.get_object().customer


@login_required(login_url='login')
def delete_button(request, id):
    delete = get_object_or_404(Contact, pk=id)
    delete.delete()
    messages.success(request, 'You have deleted your query')
    return redirect('dashboard')
