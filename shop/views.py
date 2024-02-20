import json
from django.shortcuts import render, redirect
from . models import *
from django.http import JsonResponse
from django.contrib import messages
from .forms import *
from django.contrib.auth import authenticate, login, logout

# Create your views here.

def index(request):
    product = Product.objects.filter(status = 0, trending = 0, category__status = 0)
    context = {
        'product' : product,
      }
    return render(request, "shop/index.html", context)

def collections(request):
    Category = category.objects.filter(status = 0)
    context = {
        'items' : Category,
    }
    return render(request, "shop/collections.html", context)
def collections_views(request, name):
    if (category.objects.filter(status = 0, name = name)):
        product = Product.objects.filter(category__name = name, status = 0)
        context = {
            'items' : product,
            'name' : name
        }
        # print(product)
        return render(request, "shop/product_collections.html", context)
    else:
        messages.error("No such category fount")
        return redirect(request, '/collections')

def product_details(request, cname, pname):
    if (category.objects.filter(name = cname, status = 0)):
        if (Product.objects.filter(name = pname, status = 0)):
            product = Product.objects.filter(name = pname, status = 0).first()
            context = {
                'product' : product,
                'cname' : cname,
                'pname' : pname,
            }
            # print(product.category__name)
            # print(product.name)
            return render(request, "shop/product_details.html", context)
    else:
        messages.error("No such Product fount")
        return redirect(request, '/collections')
def register(request):
    form = CustomUserCreationForm()
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your account was successfully created')
            return redirect('/home')
    
    context ={
        'form' : form
    }
    return render(request, "registration/register.html", context)

def Add_To_Cart(request):
    return JsonResponse({'status' : 'Success'}, status=200, safe=False)


def cart(request):
    cart = Cart.objects.filter(User = request.user)
    context = {
        'cart' : cart,
    }
    return render(request, "shop/cart.html", context)

def ca_delete(request, id):
    cart = Cart.objects.get(id = id)
    cart.delete()
    return redirect("/cart")
""" 
def index(request):
    return render(request, "shop/index.html") """