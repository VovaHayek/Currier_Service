from django.shortcuts import render
from django.views.generic import DetailView

from .models import Restaurant, Menu

def home_page(request):
    restaurants = Restaurant.objects.all()

    return render(request, 'home/home_page.html', {'restaurants': restaurants})

class RestaurantsDetail(DetailView):
    model = Restaurant

    def get_context_data(self, *args, **kwargs):
        context = super(RestaurantsDetail, self).get_context_data(*args, **kwargs)
        restaurant_id = self.kwargs.get('pk')
        print(restaurant_id)

        context['menu'] = Menu.objects.filter(restaurant=restaurant_id)
        return context