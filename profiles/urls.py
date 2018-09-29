from django.urls import path
from .views import ProfileDetailView, edit

app_name = 'profiles'

urlpatterns = [
	path('<str:slug>/', ProfileDetailView.as_view(), name="profile_detail"),
	path('<str:slug>/update/', edit, name="profile_update"),
]