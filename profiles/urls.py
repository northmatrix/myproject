from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from . import views

urlpatterns = [path("profile/", views.profile, name="profile"),path("edit_profile/", views.profile_edit, name="profile_edit")] 
