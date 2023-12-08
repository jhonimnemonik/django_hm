from django.shortcuts import render


def main(request):
    return render(request, 'home.html', {"page": "home"})


def contact(request):
    return render(request, 'contact.html', {"page": "contact"})
