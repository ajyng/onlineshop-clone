from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse    
from .models import Category, Product
from django.core.paginator import Paginator, EmptyPage, InvalidPage
# Paginator는 여러 개의 아이템을 페이지 단위로 관리할 수 있게 도와준다.

# Create your views here.
def index(request):
    text_var = "This is my first Django app web page!!"
    return HttpResponse(text_var)

def allProdCat(request, c_slug=None):
    c_page = None
    products_list = None

    if c_slug != None:
        c_page = get_object_or_404(Category, slug=c_slug)
        products_list = Product.objects.filter(category=c_page, available=True)
    else:
        products_list = Product.objects.all().filter(available=True)

    # Pagintor Code
    paginator = Paginator(products_list, 1)
    try:
        page = int(request.GET.get('page','3'))
    except:
        page = 1

    try:
        products = paginator.page(page)
    except(EmptyPage, InvalidPage):
        products = paginator.page(paginator.num_pages)

    return render(request, 'shop/category.html', {'category':c_page, 'products':products})

def ProdCatDetail(request, c_slug, product_slug):
    try:
        product = Product.objects.get(category__slug=c_slug, slug=product_slug)
    except Exception as e:
        raise e

    return render(request, 'shop/product.html', {'product':product})