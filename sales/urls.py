"""
URL configuration for sales project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path , include
from sales_app import views

from rest_framework.routers import DefaultRouter
from rest_framework.urlpatterns import format_suffix_patterns

router = DefaultRouter()
# router.register('orders', views.OrderViewSet, basename='order') #for ViewSets , ModelViewSets


urlpatterns = [ 
    path('admin/', admin.site.urls),

    # path('products/', views.products_list),
    path('products/<int:id>/', views.Products_Detail.as_view()),

    # path('orders/', views.OrderGenericsList.as_view()),
    # path('orders/<int:pk>/', views.OrderGenericDetail.as_view()),
    
    path('' , include(router.urls)),

    path('products/', views.Products_View.as_view()),
    path('orders/',views.Order_View.as_view()),

    path('blog/',views.Blog_View.as_view()),
    path('comments/',views.Comment_view.as_view())
]
""" # Apply format_suffix_patterns to urlpatterns
# urlpatterns = format_suffix_patterns([
#     path('products/', views.products_list),
#     path('products/<int:id>/', views.products_details),
#     ])+urlpatterns
"""