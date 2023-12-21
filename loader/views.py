from django.shortcuts import render


def photo_load(request):
    if request.method == "POST":
        uploaded_file = request.FILES.get("file")
        if uploaded_file:
            with open("loaded.png", "wb") as img_file:
                img_file.write(uploaded_file.read())
    return render(request, "photo.html", {"page": "photo"})
