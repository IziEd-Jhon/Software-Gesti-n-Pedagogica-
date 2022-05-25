from django.urls import URLPattern, path
from . import views
from AppUser.views import UploadUsersFromFileView

urlpatterns = [
    path('Student/', views.StudentList.as_view()),
    path('Student/<int:pk>',views.StudentDetail.as_view()),
    path('Teacher/', views.TeacherList.as_view()),
    path('Teacher/<int:pk>',views.TeacherDetail.as_view()),
    path('Parent/', views.ParentList.as_view()),
    path('Parent/<int:pk>',views.ParentDetail.as_view()),
    path('upload/', UploadUsersFromFileView.as_view())
]