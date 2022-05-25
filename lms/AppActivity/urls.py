from . import views
from django.urls import path

urlpatterns = [
path('Resource/', views.ResourceList.as_view()),
path('Resource/<int:pk>',views.ResourceDetail.as_view()),
]