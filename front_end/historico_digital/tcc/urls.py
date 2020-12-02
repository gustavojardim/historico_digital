from django.urls import path
from .views import services, new_service, home, root
from .auth import auth, register_user, logout

urlpatterns = [
    path("services/", services, name="services"),
    path("new_service/", new_service, name="new_service"),
    path("login/", auth, name='login'),
    path("register/", register_user, name="register"),
    path("home/", home, name="home"),
    path("logout/", logout, name="logout"),
    path("", root, name="root")
]
