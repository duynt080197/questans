from django.urls import path
from . import views
urlpatterns = [
    path('', views.home, name='home'),
    path('detail/<int:question_id>', views.detail, name='detail'),
    path('<int:question_id>/up', views.up, name="up"),
    path('<int:question_id>/down', views.down, name="down"),
    path('api/', views.GetQuestionsAPI.as_view())
]