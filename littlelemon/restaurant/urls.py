from django.urls import path
from .views import MenuItemsView, SingleMenuItemView
from rest_framework.authtoken import views

urlpatterns = [
    path('menu-items/', MenuItemsView.as_view()),
    path('menu-items/<int:pk>', SingleMenuItemView.as_view()),
    path('api-token-auth/', views.obtain_auth_token, name='api_token_auth'),
]