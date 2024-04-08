from django.contrib import admin
from django.urls import path
from app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.landing_page, name="landing_page"),
    path('note/<note_title>', views.note_details, name="note_details"),
    path("add_note", views.add_note, name="add_note"),
    path('note/<note_title>/edit', views.edit_note, name="edit_note"),
    path('note/<note_title>/delete', views.delete_note, name="delete_note")
]
