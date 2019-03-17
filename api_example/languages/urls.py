from django.urls import path, include
from .views import LanguageView
from rest_framework import routers


router = routers.DefaultRouter()
# Register views here.
router.register('languages', LanguageView)

urlpatterns = [
    path('', include(router.urls))
]