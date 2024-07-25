from django.urls import path
from api import views as api_views

urlpatterns = [
    path('user/token/', api_views.UserTOPView.as_view())
]