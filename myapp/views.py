from django.shortcuts import render


def main(request):
    return render(request, 'myapp/index.html')


def about(request):
    return render(request, 'myapp/about.html')
