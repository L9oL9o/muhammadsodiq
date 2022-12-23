from django.contrib import admin
from django.urls import path, include

from women.views import WomenAPIView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('women.urls'))
]

