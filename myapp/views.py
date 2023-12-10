from django.shortcuts import render
from myapp.forms import ContactForms


def main(request):
    return render(request, 'home.html', {"page": "home"})


def contact(request):
    clform = ContactForms()
    if request.method == "POST":
        data = request.POST
        print(data)
    return render(request, 'contact.html', {"page": "contact", "form": clform})
