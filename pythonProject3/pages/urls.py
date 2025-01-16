from django.urls import path
from . import views
urlpatterns =[
    path('',views.index,name='index'),
    path('about',views.about,name='about'),
    path('payment',views.payment,name='payment'),
    path('cart',views.cart,name='cart'),
    path('shoes',views.shoesproducts,name='shoes'),
    path('men',views.menclothes,name='men'),
    path('watches',views.watche,name='watches'),
    path('bags',views.bagsproducts,name='bags'),
    path('dresses',views.womenshirts,name='dresses'),
    path('<int:pro_id>',views.details,name='details')
]