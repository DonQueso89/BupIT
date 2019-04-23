from django.shortcuts import redirect, render


def index(request):
    """
    Serve the home page
    """
    return render(request, template_name='public/index.html')


def register(request):
    """
    This simply redirects to the user.create view now but we want to wire this
    to something more sophisticated (i.e.: something that the submits the the
    user to some audit system in stead of creating a user entry in the db directly).
    """
    if request.method == 'GET':
        return redirect('user-create')
