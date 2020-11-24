from django.urls import path
from .views import services, new_service, post_new_service
from .session import session

urlpatterns = [
    path("services/", services, name="services"),
    path("new_service/", new_service, name="new_service"),
    path("post_new_service/", post_new_service, name="post_new_service"),
    path("login/", session, name='login')
]
