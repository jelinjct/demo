from django.urls import path
app_name='cart'
from cart import views


urlpatterns = [
    path('add_cart/<int:p>/',views.add_cart,name="add_cart"),
    path('cart_view/',views.cart_view,name="cart_view"),
    path('cart_remove/<int:p>/',views.cart_remove,name="cart_remove"),
    path('full_remove/<int:p>/',views.full_remove,name="full_remove"),
    path('order',views.order,name="order"),
    path('orderview',views.orderview,name='orderview'),

]