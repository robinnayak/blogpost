from django.urls import path
from . import views
urlpatterns = [
    path('',views.UserPage,name='home'),
    path('createauthor/',views.createAuthor,name='createauthor'),
    path('success/',views.successPage,name='success'),
    path('viewauthor/<str:pk>/',views.viewAuthor,name="viewauthor"),
    path('updateauthor/<str:pk>/',views.updateAuthor,name="updateauthor"),
    path('deleteauthor/<str:pk>/',views.deleteAuthor,name="deleteauthor"),
    path('register/',views.Register,name="register"),
    path('adminregister/',views.AdminRegister,name="adminregister"),
    path('login/',views.Login,name="login"),
    path('logout/',views.LogoutPage,name="logout"),

    # path('update/<str:pk>/', Updateview, name="update"),
]
