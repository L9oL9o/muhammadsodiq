from django.urls import path
from women.views import WomenAPIView

urlpatterns = [
    path('api/v1/womenlist/', WomenAPIView.as_view()),
]
