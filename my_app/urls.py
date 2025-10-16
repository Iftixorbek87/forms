# from django.urls import path
# from .views import main
# from . import views
# urlpatterns = [
#     path ('', main, name='main-list'),
#     path('register/', register, name='register'),
#     path('panel/', views.panel, name='panel'),
#
# ]

# ✅ TO‘G‘RI
# from django.urls import path
# from . import views
#
# urlpatterns = [
#     path('', views.home, name='home'),         # bosh sahifa
#     path('register/', views.register, name='register'),  # ro‘yxatdan o‘tish
#     path('panel/', views.panel, name='panel'), # o‘zingiz yaratgan panel
#     path('panel/', views.panel, name='panel'),
# ]

from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
]