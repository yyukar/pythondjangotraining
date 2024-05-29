from django.urls import path
from . import views
urlpatterns = [
    path('',views.home),
    path('tipDetay',views.tipDetay),
    path('<link>',views.otomatikLink),
]