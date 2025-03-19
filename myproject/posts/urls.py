from django.urls import path
from . import views
# Correct
app_name= 'posts'

urlpatterns = [
    path('',views.post_list,name="list"),
    path('new-post/', views.post_new, name="new_post"),

    path("<slug:slug>",views.post_page,name="page")
]
