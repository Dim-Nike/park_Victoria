from django.shortcuts import render
from .models import *

# Create your views here.


def show_index(req):
    data = {
        'categories': CategoriesProduct.objects.all(),
        'products_is_day': Product.objects.filter(product_is_day=True),
        'products_popular': Product.objects.filter(popular=True),
        'images': MainImg.objects.all(),
        'articles': Articles.objects.all(),
    }

    return render(req, 'main/index.html', data)


def show_products(req, pk):
    data = {
        'categories': CategoriesProduct.objects.filter(id=pk),
        'products': Product.objects.filter(popular=True)
    }
    return render(req, 'main/categories.html', data)


def show_contact(req):
    data = {

    }
    return render(req, 'main/contacts.html', data)

def show_price(req):
    return render(req, 'main/1.html')