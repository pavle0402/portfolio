from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomeView, name="home"),
    path('about/', views.AboutMeView, name="about"),
    path('portfolio/', views.PortfolioView, name="portfolio"),
    path('services/', views.ServicesView, name="services"),
    path('contact/', views.ContactView, name="contact"),
    path('portfolio/<int:pk>/', views.ProjectDetailView.as_view(), name="project-detail")
]