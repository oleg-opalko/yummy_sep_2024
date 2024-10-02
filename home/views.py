from django.shortcuts import render
from home.models import Category, Dish


# Create your views here.


def index(request):

    categories = Category.objects.filter(is_visible=True).order_by('sort')

    context = {'categories': categories}

    return render(request, 'index.html', context)