from django.urls import path
<<<<<<< HEAD
from .views import PostsList, PostDetail

urlpatterns = [
    path('', PostsList.as_view()),
    path('<int:pk>', PostDetail.as_view())
=======
from .views import index

urlpatterns = [
    path('index', index)
>>>>>>> origin/master
]