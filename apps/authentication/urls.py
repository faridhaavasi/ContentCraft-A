from django.urls import path, include

app_name = 'authentication'
urlpatterns = [
    path('api/', include('apps.authentication.api.v1.urls', namespace='authentication')),
]

