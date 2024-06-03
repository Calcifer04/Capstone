from django.shortcuts import render


# VIEWS
# Home view
def home(request):
    return render(request, "home.html")


# CV view
def my_cv(request):
    return render(request, "cv.html")


# Contact me view
def contactme(request):
    return render(request, "contactme.html")
