from django.urls import path
from . import views
urlpatterns = [
    path('',views.home),
    path('yeniUye', views.yeniUye),
    path('detay/<int:uyeNo>', views.uyeDetay),
    path('duzenle/<int:uyeNo>', views.uyeDuzenle),
]