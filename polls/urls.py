from django.urls import path

from . import views

urlpatterns = [
    path('GetMedia/',views.GetMedia),
    path('SearchMedia/',views.SearchMedia),
    path('GetfrequencyTitle/',views.GetfrequencyTitle),
    path('GetfrequencyContent/',views.GetfrequencyContent)
]