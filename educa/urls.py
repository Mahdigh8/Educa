"""educa URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path, include
from courses.views import CourseListView

urlpatterns = [
    path('accounts/password_change/', 
        auth_views.PasswordChangeView.as_view(template_name="registrations/password_change_form.html"),
        name='password_change'),
    path('accounts/password_change/done/', 
        auth_views.PasswordChangeDoneView.as_view(template_name="registrations/password_change_done.html"),
        name='password_change_done'),
    path('accounts/password_reset/', 
        auth_views.PasswordResetView.as_view(
                template_name="registrations/password_reset_form.html",
                email_template_name='registrations/password_reset_email.html'),
        name='password_reset'),
    path('accounts/password_reset/done/', 
        auth_views.PasswordResetDoneView.as_view(template_name="registrations/password_reset_done.html"),
        name='password_reset_done'),
    path('accounts/reset/<uidb64>/<token>/', 
        auth_views.PasswordResetConfirmView.as_view(template_name="registrations/password_reset_confirm.html"),
        name='password_reset_confirm'),
    path('accounts/reset/done/', 
        auth_views.PasswordResetCompleteView.as_view(template_name="registrations/password_reset_complete.html"),
        name='password_reset_complete'),
	path('accounts/login/', auth_views.LoginView.as_view(template_name='registrations/login.html'), name='login'),
	path('accounts/logout/', auth_views.LogoutView.as_view(template_name='registrations/logged_out.html'), name='logout'),
    path('admin/', admin.site.urls),
    path('course/', include('courses.urls'), name='courses'),
    path('students/', include('students.urls'), name='students'),
    path('api/', include('courses.api.urls'), name='api'),
    path('profiles/', include('profiles.urls')),
    path('', CourseListView.as_view(), name='course_list'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)