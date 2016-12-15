from django.shortcuts import render
from django.utils import timezone
from .models import Product

def product_list(request):
    products = Product.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    
    return render(request, 'shopapp/product_list.html', {'products':products})
