from django.shortcuts import render,redirect
from django.contrib import messages
from pages.models import menshirts
from orders.models import Order,OrderDetails
from django.utils import timezone
def add_to_cart(request):
    #if 'pro_id' in request.Get and request.user.is_authenticated :
     #   return redirect('index' +request.Get['pro_id'])
    #else:
        return redirect('about')
# Create your views here.
