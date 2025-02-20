from django.urls import path

from apps.authentication.api.v1.views import sigin_signup

app_name = 'authentication-v1'
urlpatterns = [
    path('v1/register_stepone/', sigin_signup.SteponeRegisterView.as_view(), name='register-stepone'),
]