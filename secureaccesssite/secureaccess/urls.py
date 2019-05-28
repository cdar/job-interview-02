from django.contrib.auth import views as auth_views
from django.contrib.auth.decorators import login_required
from django.urls import path
from django.views.generic import TemplateView

from secureaccess.views import IndexView, AddElementView, RequestElementView

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('accounts/login/', auth_views.LoginView.as_view(redirect_authenticated_user=True), name='login'),
    path('accounts/logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('add_element/', AddElementView.as_view(), name='add_element'),
    path('element_added/', login_required(TemplateView.as_view(template_name='element_added.html')),
         name='element_added'
         ),
    path('request_element/<uuid:uuid>/', RequestElementView.as_view(), name='request_element')
]
