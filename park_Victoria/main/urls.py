from django.conf.urls.static import static
from django.conf import settings
from .views import *
from django.urls import path



urlpatterns = [
    path('', show_index, name='index'),
    path('products/<int:pk>', show_products, name='products'),
    path('/contact', show_contact, name='contact')

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)