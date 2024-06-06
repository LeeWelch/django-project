from django.urls import path
from . import views
# single . means current folder
# .. goes up a level

urlpatterns = [
  path("",views.home, name="home"),
  path("about",views.about, name="about"),
  path("gallery",views.gallery, name="gallery"),
  path("contact",views.contact, name="contact"),
  path('function/', views.function_view, name='function_view'),
  path('class/', views.ClassView.as_view(), name='class_view')

]
