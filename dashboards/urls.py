from django.urls import path,include
from . import views

urlpatterns = [
    #paths for category
    path('', views.dashboard,name="dashboard"),
    path('categories/',views.categories,name="categories"),
    path('categories/add',views.add_categories,name="add_categories"),
    path('categories/edit/<int:pk>',views.edit_categories,name="edit_categories"),
    path('categories/delete/<int:pk>',views.delete_categories,name="delete_categories"),
    
    #paths for posts
    path('posts/', views.posts, name="posts"),
    path('posts/add/',views.add_posts,name="add_posts"),
    path('posts/edit/<int:pk>',views.edit_posts,name="edit_posts"),
    path('posts/delete/<int:pk>',views.delete_posts,name="delete_posts"),
    
    #path for users
    
    path('users/',views.users,name='users'),
    path('users/add/',views.add_users,name='add_users'),
    path('users/edit/<int:pk>/',views.edit_users,name="edit_users"),
    path('users/delete/<int:pk>/',views.delete_users,name="delete_users")
]
