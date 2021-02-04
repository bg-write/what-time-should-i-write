from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('writers/', views.writers_index, name='index'),
    path('accounts/signup/', views.signup, name='signup'),
    path('writers/<int:writer_id>/', views.writers_detail, name='detail'),
]
