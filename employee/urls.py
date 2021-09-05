from django.urls import path
from . import views

urlpatterns=[
    path('',views.login,name='login'),
    path('dashboard/',views.dashboard,name='dashboard'),
    path('add-reply/<int:work_id>',views.add_reply,name='add_reply'),
    path('replies/<int:id>',views.replies,name='replies'),
    path('completed/',views.completed,name='completed'),
    path('logout/',views.logout,name='logout'),
]