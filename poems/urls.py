from django.urls import path
from . import views

urlpatterns = [
    path('<int:id>/', views.poem_detail, name='poem_detail'),
    path('<int:id>/createreview', views.createreview, name='createreview'),
    path('review/<int:id>', views.updatereview, name='updatereview'),
    path('review/<int:id>/delete',views.deletereview, name='deletereview'),

]