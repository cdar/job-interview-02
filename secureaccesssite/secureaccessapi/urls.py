from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token

from secureaccessapi.views import CreateElementView, GetElementView, Stats

urlpatterns = [
    path('token/', obtain_auth_token, name='token'),
    path('element/', CreateElementView.as_view(), name='create_element'),
    path('element/<uuid:uuid>/', GetElementView.as_view(), name='get_element'),
    path('stats/', Stats.as_view(), name='stats'),
]
