from django.shortcuts import render
from django.http import HttpResponse
from .models import Product, offer

# Create your views here.
def index(request):
    products = Product.objects.all()
    return render(request, 'index.html', {'products': products})
def newPrduct(request):
    return HttpResponse("Hello, world. You're at the new product page.")