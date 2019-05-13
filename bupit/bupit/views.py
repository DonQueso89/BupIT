from django.contrib.auth.decorators import login_required
from django.http import Http404
from django.shortcuts import redirect


@login_required
def login_success(request):
    """
    Intermdiate view that forces a user to choose a login type in case he/she is a student and a teacher.

    TODO: Add default login preferences to user settings
    """
    # Redirected from the login view
    if request.user.is_student and not request.user.is_teacher:
        request.session['logged_in_as'] = 'student'
        return redirect('user-detail', pk=request.user.pk)
    elif request.user.is_teacher and not request.user.is_student:
        request.session['logged_in_as'] = 'teacher'
        return redirect('user-detail', pk=request.user.pk)
    elif request.user.is_teacher and request.user.is_student:
        return redirect('login-choice')
    else:
        raise Http404("Authenticated users must have a profile")
