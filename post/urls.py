from django.contrib import admin
from django.urls import path,include
from . import views

app_name = 'post'


urlpatterns = [
    path('',views.index,name ="index"),
    path('<int:post_id>',views.detail,name ="detail"),
    path('create',views.create,name ="create"),
    path('<int:post_id>/comment',views.comment,name ="comment"),
    path('<int:post_id>/update',views.update,name ="update"),
]

