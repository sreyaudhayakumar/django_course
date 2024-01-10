from .import views
from django.urls import path
urlpatterns=[
    path('footer',views.footer,name='footer'),
    path('',views.index,name='index'),
    path('login',views.login,name="login"),
    path('dashborad',views.dashborad,name='dashborad'),
    path('add_course',views.add_course,name='add_course'),
    path('account',views.account,name='account'),
    path('courses_list',views.courses_list,name="courses_list"),
    path('edit_course/<int:product_id>/', views.edit_course, name='edit_course'),
    # path('delete_course/<int:product_id>/', views.delete_course, name='delete_course'),
    path('delete_course/<int:product_id>/', views.delete_course, name='delete_course'),
    path('edit_password/<int:user_id>/', views.edit_password, name='edit_password'),
    # path('reset_password',views.reset_password,name='reset_password'),
    path('courses_list', views.courses_list, name='courses_list'),
    path('logout', views.user_logout, name='logout'),
    path('profile',views.profile,name='profile'),
    path('short_course_create',views.short_course_create,name='short_course_create'),
#     path('short_course_view',views.short_course_view,name='short_course_view'),
]
