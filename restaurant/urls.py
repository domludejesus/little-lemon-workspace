from django.contrib import admin
from django.urls import path
from . import views
from rest_framework.routers import DefaultRouter
from .views import BookingViewSet
from rest_framework.authtoken.views import obtain_auth_token

router = DefaultRouter()
router.register(r'tables', BookingViewSet)

urlpatterns = [
   path('', views.index, name='index'),
   path('menu/', views.MenuItemView.as_view()),
   path('menu/<int:pk>', views.SingleMenuItemView.as_view()),
   path('api-token-auth/', obtain_auth_token),

] + router.urls