from django.urls import path
from . import views

#app_name = 'music'

urlpatterns = [
    # /music/
    path('', views.index, name="index"),
    # /music/a_number/
    path('<int:album_id>/', views.detail, name='detail'),
]