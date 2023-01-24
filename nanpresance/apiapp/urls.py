from rest_framework.routers import DefaultRouter
from .apiviews import *
from django.urls import path , re_path
from . import views
router = DefaultRouter()
router.register('user',ProfileViewSet,)

urlpatterns = [
        path("login_api", views.login, name="login_api"),
        path("verifqr", views.qrverif, name="verifqr"),
]


urlpatterns += router.urls