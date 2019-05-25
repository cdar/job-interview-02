from django.contrib.auth import views as auth_views
from django.urls import path

from secureaccess.views import IndexView, AddElementView

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('login', auth_views.LoginView.as_view(), name='login'),
    path('logout', auth_views.LogoutView.as_view(), name='logout'),
    path('add_element', AddElementView.as_view(), name='add_element'),
]
