from django.urls import path
from . import views

urlpatterns = [
    path('basket_list/', views.BasketListView.as_view(), name='basketList'),
    path('basket_list/<int:id>/', views.BasketDetailView.as_view(), name='basket_detail'),
    path('basket_list/<int:id>/update/', views.UpdateBasketView.as_view(), name='update_basket'),
    path('basket_list/<int:id>/delete/', views.DeleteBasketView.as_view(), name='delete_basket'),
    path('create_basket/', views.CreateBasketView.as_view(), name='createBasket'),
]