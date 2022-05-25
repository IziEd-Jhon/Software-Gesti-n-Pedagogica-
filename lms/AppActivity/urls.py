from . import views
from django.urls import path

urlpatterns = [
path('Resource/', views.ResourceList.as_view()),
path('Resource/<int:pk>',views.ResourceDetail.as_view()),
path('Folder/', views.FolderList.as_view()),
path('Folder/<int:pk>',views.FolderDetail.as_view()),
path('Archive/', views.ArchiveList.as_view()),
path('Archive/<int:pk>', views.ArchiveDetail.as_view()),
path('Activity/', views.ActivityList.as_view()),
path('Activity/<int:pk>', views.ActivityDetail.as_view()),
path('Quiz/', views.QuizList.as_view()),
path('Quiz/<int:pk>', views.QuizDetail.as_view()),
path('Assigment/', views.AssigmentList.as_view()),
path('Assigment/<int:pk>', views.AssigmentDetail.as_view()),

]