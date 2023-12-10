from django.shortcuts import redirect
from django.urls import path
from myapp import views as page

urlpatterns = [
    path('home/', page.main, name='home'),
    path('', lambda request: redirect('home')),
    path('contact/contact_process.php', page.contact_process_view, name='contact_process'),
    path('contact/', page.contact, name='contact'),
]
