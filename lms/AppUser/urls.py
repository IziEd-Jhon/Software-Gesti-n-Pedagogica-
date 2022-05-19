from django.urls import URLPattern, path
from . import views


urlpatterns = [
    path('v1/post', views.customerUser_APIView.as_view()),
    path('v1/post/<int:pk>',views.customerUser_APIView_Detail.as_view())
]