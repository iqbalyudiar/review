from django.urls import path
from . import views
from django.views.generic.base import TemplateView

urlpatterns = [
    path('', views.post_list, name='post_list'),
    # path('signup/', views.SignUp.as_view(), name='signup'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('post/new', views.post_new, name='post_new'),
    path('post/<int:pk>/edit/', views.post_edit, name='post_edit'),
    # path('', TemplateView.as_view(template_name='home.html'), name='home'),
]