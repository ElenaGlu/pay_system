from django.contrib import admin
from django.urls import path

from app import views

from app.views import CancelView, SuccessView, CreateCheckoutSessionView

urlpatterns = [

    path('cancel/', CancelView.as_view(), name='cancel'),
    path('success/', SuccessView.as_view(), name='success'),
    path('create-checkout-session/<pk>/', CreateCheckoutSessionView.as_view(), name='create-checkout-session')
    path('admin/', admin.site.urls),
]
