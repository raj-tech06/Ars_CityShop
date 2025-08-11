from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

def home(request):
    return render(request, 'home.html')

def shops(request):
    return render(request, 'shops.html')

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')

from django.shortcuts import render, redirect
from django.contrib import messages
from .models import CustomAdmin

# Static superadmin credentials
SUPERADMIN_USERNAME = "Ars_CityShop"
SUPERADMIN_PASSWORD = "Ars@CityLove"

def superadmin_login(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        if username == SUPERADMIN_USERNAME and password == SUPERADMIN_PASSWORD:
            request.session['superadmin_logged_in'] = True
            return redirect('superadmin_panel')
        else:
            messages.error(request, "Invalid username or password")
    return render(request, 'superadmin_login.html')

def superadmin_panel(request):
    if not request.session.get('superadmin_logged_in'):
        return redirect('superadmin_login')
    return render(request, 'superadmin_panel.html')



def view_admins(request):
    if not request.session.get('superadmin_logged_in'):
        return redirect('superadmin_login')
    admins = CustomAdmin.objects.all()
    return render(request, 'view_admins.html', {'admins': admins})

def active_admins(request):
    if not request.session.get('superadmin_logged_in'):
        return redirect('superadmin_login')
    admins = CustomAdmin.objects.filter(is_active=True)
    return render(request, 'active_admins.html', {'admins': admins})

def superadmin_logout(request):
    request.session.flush()
    return redirect('superadmin_login')




def create_admin(request):
    if not request.session.get('superadmin_logged_in'):
        return redirect('superadmin_login')

    if request.method == "POST":
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        shop_name = request.POST.get('shop_name')
        shop_address = request.POST.get('shop_address')
        mobile_number = request.POST.get('mobile_number')

        CustomAdmin.objects.create(
            username=username,
            email=email,
            password=password,
            shop_name=shop_name,
            shop_address=shop_address,
            mobile_number=mobile_number
        )
        messages.success(request, "Admin created successfully!")
        return redirect('create_admin')

    return render(request, 'create_admin.html')



# for admin---------------

def admin_login(request):
    if request.method == "POST":
        email = request.POST.get('email')
        password = request.POST.get('password')

        try:
            admin = CustomAdmin.objects.get(email=email, password=password)
            request.session['admin_logged_in'] = True
            request.session['admin_id'] = admin.id
            return redirect('admin_dashboard')
        except CustomAdmin.DoesNotExist:
            messages.error(request, "Invalid email or password")
    
    return render(request, 'admin_login.html')


def admin_dashboard(request):
    if not request.session.get('admin_logged_in'):
        return redirect('admin_login')
    
    admin = CustomAdmin.objects.get(id=request.session['admin_id'])
    return render(request, 'admin_dashboard.html', {'admin': admin})


def admin_logout(request):
    request.session.flush()
    return redirect('admin_login')


# for admin after login--------------

from django.shortcuts import render

def admin_dashboard(request):
    return render(request, "admin_dashboard.html")


# views.py
from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required
def add_product(request):
    return render(request, 'add_product.html')

@login_required
def selling_history(request):
    return render(request, 'selling_history.html')

@login_required
def my_sales(request):
    return render(request, 'my_sales.html')

@login_required
def manage_products(request):
    return render(request, 'manage_products.html')


