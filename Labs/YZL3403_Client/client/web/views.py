from django.shortcuts import render, redirect
import requests
from .forms import CategoryForm
from .models import Category

# Create your views here.


def get_all_categories(request):
    url = 'http://127.0.0.1:8000/'
    response = requests.get(url)
    try:
        if response.status_code == 200:
            print(response.json())
    except requests.RequestException as err:
        print(f'Request failed. {err}')

    return render(request, 'categories.html', {'categories': response.json()})


def get_categories_by_id(request, id):
    url = f'http://127.0.0.1:8000/category/{id}'
    response = requests.get(url)
    try:
        if response.status_code == 200:
            print(response.json())
    except requests.RequestException as err:
        print(f'Request failed. {err}')

    return render(request, 'detail.html', {'category': response.json()})


def create_category(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST)

        if form.is_valid():
            url = 'http://127.0.0.1:8000/category/create'

            requests.post(url, json=form.cleaned_data)

            return redirect('categories')
    else:
        form = CategoryForm

    return render(request, 'create.html', {'form': form})


def update_category(request, id):
    url = f'http://127.0.0.1:8000/category/{id}'
    category = requests.get(url)

    try:
        if category.status_code == 200:
            print(category.json())
    except requests.RequestException as err:
        print(f'Request failed. {err}')

    if request.method == 'POST':
        form = CategoryForm(request.POST)

        if form.is_valid():
            response = requests.put(url, json=form.cleaned_data)
            print(response)

            return redirect('categories')
    else:
        form = CategoryForm()

    return render(request, 'update.html', {'form': form})


def delete_category(request, id):
    url = f'http://127.0.0.1:8000/category/{id}'
    response = requests.delete(url)
    print(response)

    return redirect('categories')


