from django.urls import path
from myapp import views as home

urlpatterns = [
    path('', home.main, name='home'),
    path('home/', home.main, name='home'),
    # path('about/', home.about, name='about')
]
