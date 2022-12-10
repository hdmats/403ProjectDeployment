from django.urls import path
from .views import indexPageView, safetyPageView, infoPageView
from .views import showSightingPageView, updateSightingPageView, addSightingPageView, deleteSightingPageView

urlpatterns = [
    path("safety/", safetyPageView, name='safety'),
    path("info/", infoPageView, name='info'),
    path("showSighting/<int:sighting_id>/", showSightingPageView, name="showSighting"),
    path("updateSighting/", updateSightingPageView, name="updateSighting"),
    path("addSighting/", addSightingPageView, name="addSighting"),
    path("deleteSighting/<int:sighting_id>/", deleteSightingPageView, name="deleteSighting"),
    path("", indexPageView, name='index'),
]