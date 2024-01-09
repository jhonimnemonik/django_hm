from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib import messages
from myapp.forms import ContactForms


def main(request):
    return render(request, 'home.html', {"page": "home"})


def contact(request):
    cform = ContactForms()
    if request.method == "POST":
        data = request.POST
        print(data)
        cform = ContactForms(data)
        if cform.is_valid():
            cform.save()
            messages.success(request, 'Ваше сообщение успешно отправлено!')
            return HttpResponseRedirect(request.path)
        else:
            messages.error(request, 'Пожалуйста, исправьте ошибки в форме.')
    return render(request, 'contact.html', {"page": "contact", "form": cform})
