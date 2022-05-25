from django.urls import URLPattern, path
from . import views


urlpatterns = [
    path('Student/', views.StudentList.as_view()),
    path('Student/<int:pk>',views.StudentDetail.as_view()),
    path('Teacher/', views.TeacherList.as_view()),
    path('Teacher/<int:pk>',views.TeacherDetail.as_view()),
    path('Parent/', views.ParentList.as_view()),
<<<<<<< Updated upstream
=======
    path('Parent/<int:pk>',views.ParentDetail.as_view()),
    path('Annotation/', views.AnnotationList.as_view()),
    path('Annotation/<int:pk>', views.AnnotationDetail.as_view()),
    path('EnrollmentSubject/', views.EnrollmentSubjectList.as_view()),
    path('EnrollmentSubject/<int:pk>', views.EnrollmentSubjectDetail.as_view()),
    path('EnrollmentCourse/',views.EnrollmentCourseList.as_view()),
    path('EnrollmentCourse/<int:pk>',views.EnrollmentCourseDetail.as_view()),
    
>>>>>>> Stashed changes
]