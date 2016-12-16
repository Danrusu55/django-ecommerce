from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Product

def product_list(request):
    products = Product.objects.filter(published_date__lte=timezone.now()).order_by('published_date')

    return render(request, 'shopapp/product_list.html', {'products':products})
def product_detail(request, pk):
    product = get_object_or_404(Product,pk=pk)
    return render(request,'shopapp/product_detail.html', {'product': product})
