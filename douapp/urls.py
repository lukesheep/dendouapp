from django.urls import path
from .views import report, list_result, owntama, update
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('report/', report.as_view(), name="report"),
    path('dormitop/', views.dormitop, name="dormitop"),
    path('list_result/', list_result.as_view(), name="list_result"),
    path('owntama/', owntama.as_view(), name="owntama"),
    path('search/', views.search, name="search"),
    path('place/<str:ku>', views.place, name="place"),
    path('p_detail/<str:dplace>/', views.p_detail, name="p_detail"),
    path('tamashi/<int:pk>/', views.tamashi, name="tamashi"),
    path('tamashi/<int:pk>/update/', update.as_view(), name="update"),

]
