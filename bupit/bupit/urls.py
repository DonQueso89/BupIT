"""bupit URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import include, path
from public.forms import UserAuthenticationForm
from . import views


# LoginView takes some work out of our hands.
# See https://devdocs.io/django~2.1/topics/auth/default#django.contrib.auth.views.LoginView
login_view = LoginView.as_view(
    template_name='public/login.html',
    redirect_authenticated_user=True,
    authentication_form=UserAuthenticationForm,
)

# redirects to settings.LOGOUT_REDIRECT_URL
logout_view = LogoutView.as_view()

urlpatterns = [
    path('', include('public.urls')),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('loginsuccess/', views.login_success, name='login-success'),
    path('admin/', admin.site.urls),
    path('students/', include('students.urls')),
    path('teachers/', include('teachers.urls')),
    path('users/', include('users.urls')),
]
