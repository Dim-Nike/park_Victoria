from django.shortcuts import render
from .models import *

# Create your views here.


def show_test(req):
    data = {'products': ['name_1', 'name_2', 'name_3'],
            'blogs': ['blog_1', 'blog_2', 'blog_3']
            }
    return render(req, 'main/test.html', data)

def show_test2(req):

    return render(req, 'main/test_2.html')

def show_index(req):
    return render(req, 'main/index.html')