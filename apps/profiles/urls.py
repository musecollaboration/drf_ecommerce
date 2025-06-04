from django.urls import path

from apps.profiles.views import OrderItemsView, OrdersView, ProfileView, ShippingAddressesView, ShippingAddressViewID

urlpatterns = [
    path("", ProfileView.as_view()),
    path("shipping_addresses/", ShippingAddressesView.as_view()),
    path("shipping_addresses/detail/<uuid:id>/", ShippingAddressViewID.as_view()),
    path("orders/", OrdersView.as_view()),
    path("orders/<str:tx_ref>/", OrderItemsView.as_view()),
]
