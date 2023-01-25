from django.urls import path
from .views import *

urlpatterns = [
    path("register", get_register, name="register"),
    path("login", get_login, name="login"),
    path("logout", get_logout, name="logout"),

    path("", get_userlist, name="artist-user"),
    path("update-user/<int:pk>", user_update, name="update-user"),
    path("delete-user/<int:pk>/", user_delete, name="delete-user"),

    path("artist-list", get_artistlist, name="artist-list"),
    path("add-artist", createartist, name="add-artist"),
    path("update-artist/<int:pk>", artist_update, name="update-artist"),
    path('artist-delete/<int:pk>',delete_artist,name='artist-delete'),

    path('view-music/<int:pk>',view_music,name='view-music'),
    path('music-update/<int:pk>',music_update,name='music-update'),
    path('music-delete/<int:pk>',delete_music,name='music-delete'),


    

    
   
]
