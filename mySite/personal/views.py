from django.shortcuts import render


# VIEWS
# Home view
def home(request):
    """ Used in urls.py to show home.html upon empty url path.
        Handles Http requests & renders home.html in response.
    :param request: HttpRequest
    :type request: Any
    :return: Rendered view of home.html
    :rtype: HttpResponse
    """
    return render(request, "home.html")


# CV view
def my_cv(request):
    """Used in urls.py to show cv.html upon 'cv/' url path specification.
        Handles Http requests & renders cv.html in response.
    :param request: HttpRequest
    :type request: Any
    :return: Rendered view of cv.html
    :rtype: HttpResponse
    """
    return render(request, "cv.html")


# Contact me view
def contactme(request):
    """Used in urls.py to show contactme.html upon 'contactme/' url path specification.
        Handles Http requests & renders contactme.html in response.
    :param request: HttpRequest
    :type request: Any
    :return: Rendered view of contactme.html
    :rtype: HttpResponse
    """
    return render(request, "contactme.html")
