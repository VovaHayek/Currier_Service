from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate, logout
from django.views.generic import DetailView
from django.contrib import messages

from .forms import NewUserForm
from .models import Restaurant, Menu

def home_page(request):
    restaurants = Restaurant.objects.all()

    return render(request, 'home/home_page.html', {'restaurants': restaurants})

class RestaurantsDetail(DetailView):
    model = Restaurant

    def get_context_data(self, *args, **kwargs):
        context = super(RestaurantsDetail, self).get_context_data(*args, **kwargs)
        restaurant_id = self.kwargs.get('pk')

        context['menu'] = Menu.objects.filter(restaurant=restaurant_id)
        return context
    
def user_registration(request):
    if request.method == "POST":
        print('WORKS')
        form = NewUserForm(request.POST)
        if form.is_valid():
            print("VALID!!!")
            user = form.save()
            login(request, user)
            return redirect('/')
        
    form = NewUserForm()
    return render(request, template_name="main/register.html", context={"register_form": form})

def user_login(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('/')
            else:
                messages.error(request, 'Invalid username or password')
        else:
            messages.error(request,"Invalid username or password.")

    form = AuthenticationForm()
    return render(request, "main/login.html")

def user_logout(request):
    logout(request)
    return redirect('/')