from django.conf import settings
from django.urls import path
from . import views
from django.conf.urls.static import static

urlpatterns = [
    path('',views.main,name = 'main'),
    path('store/',views.store,name = 'store'),
    path('feedback/',views.feedback,name='feedback'),
    path('galary/',views.galary,name='galary'),
    path('mp/',views.mp,name='mp'),
    path('mp/<str:num>/', views.infa_of_mp,name='infa_of_mp'),
    path('information/',views.information,name='information'),
    path('vacance/',views.vacance,name='vacance'),
    path('store/<str:num>/', views.store_chapter,name='store_chapter'),
    path('reservation/',views.reservation,name = 'reservation')
]
