from django.shortcuts import render
from .models import *

# Create your views here.


def show_index(req):
    data = {
        'categories': CategoriesProduct.objects.all(),
        'products': Product.objects.all()
    }

    return render(req, 'main/index.html', data)