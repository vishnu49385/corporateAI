from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name= 'index'),
    path('products/', views.products, name='products'),
    path('services/', views.services, name='services'),
    path('contact-us/', views.contact, name='contact'),
    path('about-us/', views.about, name='about')
]
