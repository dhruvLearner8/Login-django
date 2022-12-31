from django.urls import path
from . import views


urlpatterns = [
    #path("",views.home,name='home'),
    path("",views.register,name="register"),
    path("login",views.login,name="login"),
    path("home",views.home,name="home"),
    path("logout",views.logout,name="logout"),
    path("alluser",views.admin_users),
]

# from django.urls import path
# from .views import UserDetailAPI,RegisterUserAPIView
# urlpatterns = [
#   path("get-details",UserDetailAPI.as_view()),
#   path('register',RegisterUserAPIView.as_view()),
# ]