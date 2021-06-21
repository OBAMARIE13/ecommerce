from django.shortcuts import render
from service import models as models_service


def index(request):
    article = models_service.Articles.objects.filter(status=True)
    categorie = models_service.Categorie_articles.objects.filter(status=True)
    marque = models_service.Marques_articles.objects.filter(status=True)
    return render(request, 'index.html', locals())

def cart(request):
    return render(request, 'cart.html')

def checkout(request):
    return render(request, 'checkout.html')

def product_detail(request):
    return render(request, 'product-details.html')

def shop(request):
    articles = models_service.Articles.objects.filter(status=True)
    categorie = models_service.Categorie_articles.objects.filter(status=True)
    marque = models_service.Marques_articles.objects.filter(status=True)
    return render(request, 'shop.html', locals())
# Create your views here.
