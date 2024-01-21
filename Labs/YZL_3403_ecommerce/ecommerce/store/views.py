from django.db.models import Q
from django.shortcuts import render
from .models import Product, Category

# Create your views here.


def store(request):
    all_products = Product.objects.values('title', 'price', 'image', 'slug').filter(Q(status='Active') | Q(status='Modified')).order_by('title')

    # region For Test
    # for product in all_products:
    #     print(f'Title: {product["title"]}\n'
    #           f'Slug: {product["slug"]}\n'
    #           f'Image: {product["image"]}')
    #
    # print(all_products.count())
    # endregion

    return render(request, 'store.html', {'all_products': all_products})


def categories(request):
    model = Category.objects.filter(Q(status='Active') | Q(status='Modified')).values('name', 'slug').order_by('name')

    # ecommerce => settings => TEMPLATES[] listesine register edilecek.
    return {'model': model}


def list_category(request, category_slug=None):
    # 1.adım: fonksiyona gelen category_slug bilgisi ile category tablosuna sorgu atılarak ilgili slug'a ait category bilgileri getirilir. Bu bilgilerden de sadece id'ye ihtiyacımız var.
    category = Category.objects.filter(Q(status='Active') | Q(status='Modified'), Q(slug=category_slug)).values('id', 'name').first()

    # 2.adım: Yukarıda bulduğumuz category id bilgisine ait ürünleri listeliyoruz
    model = Product.objects.filter(Q(status='Active') | Q(status='Modified'), Q(category_id=category['id'])).values('title', 'price', 'image', 'slug').order_by('title')

    return render(request, 'list-category.html', {'category_name': category['name'], 'products': model})


def product_info(request, product_slug):
    data = Product.objects.select_related('category').filter(Q(status='Active') | Q(status='Modified'), Q(slug=product_slug)).values('title', 'description', 'price', 'image', 'brand', 'category__name').first()

    return render(request, 'product-info.html', {'product_info': data})
