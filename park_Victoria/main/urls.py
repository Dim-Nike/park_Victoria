from django.conf.urls.static import static
from django.conf import settings
from .views import *
from django.urls import path



urlpatterns = [
    path('index/', show_index, name='index'),
    path('products/<int:pk>', show_products, name='products')

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)