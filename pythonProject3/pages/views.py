from django.shortcuts import render,get_object_or_404,redirect
from django.http import HttpResponse
from .models import shoes
from .models import watches
from .models import dresses
from .models import bags
from .models import menshirts



# Create your views here.
def index(request):
    context = {
        'shoes': shoes.objects.all(),
        'watches': watches.objects.all(),
        'dress': dresses.objects.all(),
        'bag': bags.objects.all(),
        'shirts':menshirts.objects.all()

    }

    return render(request, 'pages/index.html',context)

def about(request):
    return render(request, 'pages/about.html')
def payment(request):
    return render(request, 'pages/payment.html')
def cart(request):
    return render(request,'pages/cart.html')
def shoesproducts (request):
    shoe = shoes.objects.all()
    name = None
    if 'searchname' in request.GET:
        name=request.GET['searchname']
        if name:
            shoe = shoe.filter(name__icontains=name)

    context = {
        'shoes': shoe

    }
    return render(request,'pages/shoesproducts.html',context)

def menclothes (request):
    shirt = menshirts.objects.all()
    name = None
    if 'searchname' in request.GET:
        name = request.GET['searchname']
        if name:
            shirt = shirt.filter(name__icontains=name)

    context = {
        'shirts': shirt

    }
    return render(request,'pages/menclothes.html',context)

def watche (request):
    watch = watches.objects.all()
    name = None
    if 'searchname' in request.GET:
        name = request.GET['searchname']
        if name:
            watch = watch.filter(name__icontains=name)

    context = {
        'watches': watch

    }
    return render(request,'pages/watches.html',context)

def womenshirts (request):
    dress = dresses.objects.all()
    name = None
    if 'searchname' in request.GET:
        name = request.GET['searchname']
        if name:
            dress = dress.filter(name__icontains=name)

    context = {
        'dresses': dress

    }
    return render(request,'pages/dresses.html',context)

def bagsproducts (request):
    bag = bags.objects.all()
    name = None
    if 'searchname' in request.GET:
        name = request.GET['searchname']
        if name:
            bag = bag.filter(name__icontains=name)

    context = {
        'bags': bag

    }
    return render(request,'pages/bags.html',context)

def details(request,pro_id):
    context = {'men': get_object_or_404(menshirts,pk=pro_id)}
    return render(request, 'pages/Details.html')
