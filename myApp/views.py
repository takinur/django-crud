from calendar import c
from multiprocessing import context
from django.shortcuts import get_object_or_404, redirect, render

from myApp.forms import ProductForm
# import product and category from models
from .models import Category, Product

# Create your views here.


def index(request):
    return render(request, 'index.html')


def listProduct(request, category_slug=None):
    categories = None
    products = None

    if category_slug != None:
        categories = get_object_or_404(Category, slug=category_slug)
        products = Product.objects.filter(category=categories)
    else:
        products = Product.objects.all().order_by('-id')

    # paginator = Paginator(products, 10)
    # page = request.GET.get('page')
    # paged_products = paginator.get_page(page)

    context = {'products': products, }

    return render(request, 'ShopApp/listProduct.html', context)


def createProduct(request):
    if request.method == "POST":
        form = ProductForm(request.POST)

        if form.is_valid():
            form.save()
            # messages.success(request, ('Data Inserted Succesfully!'))
            return redirect('list')
    else:
        form = ProductForm()
    
    context = {'form': form, 'title' : 'Create new Product'}
    return render(request, 'ShopApp/createProduct.html', context)
