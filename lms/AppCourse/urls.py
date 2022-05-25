from django.urls import URLPattern, path
from . import views


urlpatterns = [
    path('Course/', views.CourseList.as_view()),
    path('Course/<int:pk>',views.CourseDetail.as_view()),
    path('Subject/', views.SubjectList.as_view()),
    path('Subject/<int:pk>',views.SubjectDetail.as_view()),
    path('Section/', views.SectionList.as_view()),
    path('Section/<int:pk>', views.SectionDetail.as_view()),

]