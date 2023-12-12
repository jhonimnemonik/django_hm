from django.shortcuts import render
from myapp.forms import ContactForms
from django.http import HttpResponseRedirect


def main(request):
    return render(request, 'home.html', {"page": "home"})


def contact(request):
    clform = ContactForms()
    if request.method == "POST":
        data = request.POST
        print(data)
        return HttpResponseRedirect(request.path)
    return render(request, 'contact.html', {"page": "contact", "form": clform})
