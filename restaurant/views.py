from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from .models import Dish, Reservation
from .forms import DishForm, ReservationForm, RegisterForm
from django.contrib import messages


def home(request):
    dishes = Dish.objects.all()
    return render(request, 'restaurant/home.html', {'dishes': dishes})


def menu(request):
    query = request.GET.get('q')
    if query:
        dishes = Dish.objects.filter(name__icontains=query)
    else:
        dishes = Dish.objects.all()
    category = request.GET.get('c')
    if category:
        dishes = Dish.objects.filter(category__iexact=category)
    else:
        dishes = Dish.objects.all()

    paginator = Paginator(dishes, 6)
    page = request.GET.get('page')
    dishes = paginator.get_page(page)

    return render(request, 'restaurant/menu.html', {'dishes': dishes})
def dish_detail(request, pk):
    dish=get_object_or_404(Dish, pk=pk)
    return render(request, 'restaurant/dish_detail.html',{'dish' : dish})

@login_required
def add_dish(request):
    if request.method == 'POST':
        form = DishForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "Dish added successfully!")
            return redirect('menu')
    else:
        form = DishForm()
    return render(request, 'restaurant/add_dish.html', {'form': form})


@login_required
def edit_dish(request, pk):
    dish = get_object_or_404(Dish, pk=pk)
    if request.method == 'POST':
        form = DishForm(request.POST, request.FILES, instance=dish)
        if form.is_valid():
            form.save()
            messages.success(request, "Dish updated successfully!")
            return redirect('menu')
    else:
        form = DishForm(instance=dish)
    return render(request, 'restaurant/edit_dish.html', {'form': form})


@login_required
def delete_dish(request, pk):
    dish = get_object_or_404(Dish, pk=pk)
    if request.method == 'POST':
        dish.delete()
        messages.success(request, "Dish deleted successfully!")
        return redirect('menu')
    return render(request, 'restaurant/delete_dish.html', {'dish': dish})

@login_required
def reserve(request):
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            reservation = form.save(commit=False)
            reservation.user = request.user
            reservation.save()
            messages.success(request, "Reservation made successfully!")
            return redirect('profile')
    else:
        form = ReservationForm()
    return render(request, 'restaurant/reserve.html', {'form': form})


@login_required
def profile(request):
    reservations = Reservation.objects.filter(user=request.user)
    return render(request, 'restaurant/profile.html', {'reservations': reservations})


def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Account created successfully! You can now login.")
            return redirect('login')
    else:
        form = RegisterForm()
    return render(request, 'restaurant/register.html', {'form': form})


def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            messages.success(request, "Logged in successfully!")

            # Check if user is admin/staff
            if user.is_staff:
                return redirect('/admin/')
            else:
                return redirect('home')
        else:
            messages.error(request, "Invalid username or password")
            return render(request, 'restaurant/login.html')
    return render(request, 'restaurant/login.html')


def logout_view(request):
    logout(request)
    messages.success(request, "Logged out successfully!")
    return redirect('home')
