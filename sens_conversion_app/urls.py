from django.urls import path
from . import views

urlpatterns = [
    path("",views.index,name="index"),
    path("edpi_calculator/", views.edpi_calculator,name="edpi_calculator"),
    path("download_sensitivities/",views.download_sensitivities,name="download_sensitivities"),
]