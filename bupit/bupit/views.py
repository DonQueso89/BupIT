from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect


@login_required
def login_success(request):
    """
    intermediate view that redirects to the user-detail of the logged in user
    """
    return redirect('user-detail', pk=request.user.pk)
