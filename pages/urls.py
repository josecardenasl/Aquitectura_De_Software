from django.urls import path
from .views import HomePageView, AboutPageView, ProductIndexView, ProductShowView, ProductCreateView, ContactPageView, ProductCreatedView

 
 
urlpatterns = [ path('', HomePageView.as_view(), name='home'),
               path('contact/', ContactPageView.as_view(), name='contact'),
               path('about/', AboutPageView.as_view(), name='about'),
               path('products/', ProductIndexView.as_view(), name='index'),
               path('products/create', ProductCreateView.as_view(), name='form'),
               path('products/<str:id>', ProductShowView.as_view(), name='show'),
               path('products/created/', ProductCreatedView.as_view(), name='product-created'),

               

               
]