from django.shortcuts import render


def login(request):
    """
    Serve the login page
    """
    return render(request, template_name='public/login.html')
