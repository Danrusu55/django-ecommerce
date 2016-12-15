from django.shortcuts import render

def product_list(request):
    return render(request, 'shopapp/product_list.html', {})
