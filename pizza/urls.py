
from django.urls import path
from django.conf import settings
from .views import *


urlpatterns = [
    path('', Homepage.as_view(), name = 'home'),
    path('<int:pk>/', Detailpage.as_view(), name = 'detail'),
    path('createpage/', Createpage.as_view(), name = 'create'),
    path('createpage/createpizza/', Createpizza.as_view(), name = 'create_pizza'),    
    path('<int:pk>/update/', UpdatePizza.as_view(), name = 'update'),
    path('<int:pk>/adminupdate/', AdminUpdatePizza.as_view(), name = 'admin_update'),    
    path('<int:pk>/checkout/', Confirmpage.as_view(), name = 'checkout'),
    path('<int:pk>/delete/', DeletePizza.as_view(), name = 'delete'),
    path('<int:pk>/checkout/buy/', Buypage.as_view(), name = 'buy'),
    path('accounts/profile', userProfile, name='profile'),
    path('createS/', CreateStore.as_view(), name='create_store'),
    path('createS/createStore/', CreateStoreee.as_view(), name='createStore'),

]
