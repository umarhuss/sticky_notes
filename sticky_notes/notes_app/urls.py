from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('notes_hub/', views.notes_hub, name='notes_hub'),
    path('add_note/', views.add_note, name='add_note'),
    path('edit_note/<int:note_id>/', views.edit_note, name='edit_note'),
    path('note/<int:note_id>/', views.view_note, name='view_note'),
    path('delete/<int:note_id>/', views.delete_note, name='delete_note'),
    path('register/', views.register, name='register_user'),
    path('login/', views.log_in, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
]
