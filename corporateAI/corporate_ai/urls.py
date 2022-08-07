from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name= 'index'),
    path('products/cad-design/', views.cad_detail, name='cad'),
    path('products/graphic-design/', views.graphic_detail, name='graphic-design'),
    path('products/carbon-capture-equipment/', views.cce_detail, name='cce'),
    path('products/', views.products, name='products'),
    path('services/', views.services, name='services'),
    path('contact-us/', views.contact, name='contact'),
    path('about-us/', views.about, name='about')
]
