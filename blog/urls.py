from django.contrib import admin
from django.urls import include, path
from . import views


app_name = 'view_blog'

urlpatterns = [
    path('', views.home,  name = 'home'),
    path('posts/', views.view_all_publi_posts,  name = 'all_publi_posts'),
    path('login/', views.login_view,  name = 'login'),
    path('logout/', views.logout_view,  name = 'logout'),
    path('tech/<int:tech_pk>', views.view_all_publi_posts, name = 'view_all_publi_posts_tech'),
    
    path('manage/', views.view_all_unpubli_posts,  name = 'all_unpubli_posts'),
    path('new_post/', views.create_post,  name = 'create_post'),
    path('edit_post/<int:pk>', views.edit_post,  name = 'edit_post'),
    path('delete/<int:pk>', views.delete_post, name = 'delete_post'),
    path('view/<int:pk>', views.view_post, name = 'view_post'),
    path('published/<int:pk>/<str:publi>', views.change_post_status, name = 'change_post_status'),
]
