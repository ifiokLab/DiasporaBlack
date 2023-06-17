

from . import views 
from django.urls import path

urlpatterns = [
   path('',views.Home,name='home'),
   path('logout/',views.Logout,name='logout'),
   path('customer-signup/',views.customer_signup, name='customer_signup'),
   path('customer-login/',views.customer_login.as_view(), name='customer_login'),
   path('product-detail/<int:pk>/',views.product_detail,name='product_detail'),
   #path('product-cart/',views.product_cart,name='product_cart'),

   path ('order-summary', views.OrderSummaryView.as_view(), name='order-summary'),
   path ('add-to-cart/<int:pk>/', views.add_to_cart, name='add-to-cart'),
   path ('remove-from-cart/<int:pk>/', views.remove_from_cart, name='remove-from-cart'),
   path ('reduce-quantity-item/<int:pk>/', views.reduce_quantity_item, name='reduce-quantity-item'),
   path('account/',views.customer_account,name='customer-account'),
   path('customer/address/create/',views.create_customer_address,name='create-customer-address'),
 
   path ('checkout/', views.CheckoutView.as_view(), name='checkout'),
   path ('payment/', views.PaymentView.as_view(), name='payment'),
   path('customer/checkout/address/',views.CheckoutAddress.as_view(),name = 'checkout-address'),
   path('save-product/<int:productId>/',views.save_product,name='save-product'),
   path('remove-save-product/<int:productId>/',views.remove_save_product,name='save-product'),
   path('save-later/',views.SaveLater,name='save-later'),

   path('seller-login/',views.seller_login.as_view(),name='seller-login'),
   path('seller-signup/',views.seller_signup,name='seller-signup'),
   path('seller-dashboard/',views.seller_dashboard,name='seller-dashboard'),
   path('seller-orders/',views.seller_orders,name='seller-orders'),
   path('seller-customer/',views.seller_customer,name='seller-customer'),
   path('seller-settings/',views.seller_settings,name='seller-settings'),
   path('create-product/',views.create_product,name='create-product'),
   path('product-list/',views.product_list,name='product-list'),
   path('edit-product/<int:pk>/',views.edit_product,name='edit-product'),

   
]