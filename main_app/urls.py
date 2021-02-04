from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('writers/', views.writers_index, name='index'),
    path('accounts/signup/', views.signup, name='signup'),
    path('writers/<int:writer_id>/', views.writers_detail, name='detail'),
    # Will have to update; I want users to be able to upload a request for a writer to add. I do NOT want users to upload these writers themselves. I want all that to happen through the backend.
    path('writers/create/', views.WriterCreate.as_view(), name='writers_create'),
]
