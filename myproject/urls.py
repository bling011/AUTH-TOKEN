from django.contrib import admin
from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token
from myapp.views import SecureHelloView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-token-auth/', obtain_auth_token),
    path('secure-hello/', SecureHelloView.as_view()),
]
