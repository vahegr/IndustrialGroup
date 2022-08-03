from django.shortcuts import render
from product_app.models import Product
from django.core.paginator import Paginator


def product_items(request):
    pro = Product.objects.filter(allowing=True)
    pagination = Paginator(Product.objects.filter(allowing=True), 6)
    page = request.GET.get('page')
    product = pagination.get_page(page)
    return render(request, 'product_app/products.html', context={'product': pro, 'pro': product})


def product_detail(request, id, slug):
    detail = Product.objects.get(id=id, slug=slug)
    return render(request, 'product_app/product_detail.html', context={'detail': detail})
