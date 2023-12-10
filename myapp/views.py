from django.shortcuts import render


def main(request):
    return render(request, 'home.html', {"page": "home"})


def contact_process_view(request):
    data = request.POST
    print(data)
    return render(request, 'contact.html', {"page": "contact"})


def contact(request):
    if request == "POST":
        data = request.POST
        print(data)
    return render(request, 'contact.html', {"page": "contact"})
