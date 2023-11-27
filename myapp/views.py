from django.shortcuts import render


def main(request):
    return render(request, 'home.html')


# def about(request):
#     return render(request, 'myapp/about.html')
