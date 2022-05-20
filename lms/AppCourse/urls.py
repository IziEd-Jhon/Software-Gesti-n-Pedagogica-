from django.urls import URLPattern, path
from . import views


urlpatterns = [
    path('Course/', views.CourseList.as_view()),
    path('Course/<int:pk>',views.CourseList.as_view()),

]