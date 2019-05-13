from logging import getLogger
from django.contrib.auth.decorators import login_required
from django.http import Http404
from django.shortcuts import render, redirect
from public import forms as public_forms

logger = getLogger(__name__)


def index(request):
    """
    Serve the home page
    """
    return render(
        request,
        template_name='public/index.html',
        context={'login_form': public_forms.UserAuthenticationForm()}
    )


def register(request, register_as):
    profile_form_class = {
        'leerling': public_forms.StudentRegistrationForm,
        'leraar': public_forms.TeacherRegistrationForm,
    }.get(register_as)

    if not profile_form_class:
        raise Http404

    if request.method == 'GET':
        ctx = {
            'register_as': register_as,
            'user_form': public_forms.UserRegistrationForm(),
            'profile_form': profile_form_class(),
            'login_form': public_forms.UserAuthenticationForm()
        }

        return render(
            request,
            template_name='public/registration.html',
            context=ctx,
            status=200
        )
    else:
        user_form = public_forms.UserRegistrationForm(request.POST)
        profile_form = profile_form_class(request.POST, request.FILES)

        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            profile = profile_form.save(commit=False)
            profile.user = user
            profile.save()
            return redirect('registration-success')

        return render(
            request,
            template_name='public/registration.html',
            context={
                'user_form': user_form,
                'profile_form': profile_form,
                'register_as': register_as,
                'login_form': public_forms.UserAuthenticationForm()
            },
            status=200
        )


def registration_success(request):
    return render(
        request,
        template_name='public/registration_success.html',
        context={
            'login_form': public_forms.UserAuthenticationForm()
        },
    )


def registration_choice(request):
    return render(
        request,
        template_name='public/registration_choice.html',
    )


@login_required
def login_choice(request):
    if request.method == 'GET':
        return render(
            request,
            template_name='public/login_choice.html',
        )
    else:
        logged_in_as = request.POST.get('log_in_as')
        if not logged_in_as or logged_in_as not in ('student', 'teacher'):
            raise Http404("Somebody is messing with post data")
        elif logged_in_as == 'student' and not request.user.is_student:
            raise Http404("Path not allowed for this user")
        elif logged_in_as == 'teacher' and not request.user.is_teacher:
            raise Http404("Path not allowed for this user")
        else:
            request.session['logged_in_as'] = logged_in_as
            return redirect('user-detail', pk=request.user.id)
