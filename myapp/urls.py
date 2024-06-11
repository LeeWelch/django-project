from django.urls import path
from . import views
from .views import InventionListView, InventionDetailView

# single . means current folder
# .. goes up a level

urlpatterns = [
  path("",views.home, name="home"),
  path("about",views.about, name="about"),
  path("gallery",views.gallery, name="gallery"),
  path("contact",views.contact, name="contact"),
  path('function/', views.function_view, name='function_view'),
  path('class/', views.ClassView.as_view(), name='class_view'),
  path('theme/', views.ThemeView.as_view(), name='theme'),
  path('load/', views.load_default_data_view, name='load_default_data'),
  path('inventions/', InventionListView.as_view(), name='invention-list'),
  path('invention/<int:pk>/', InventionDetailView.as_view(), name='invention-view'),


]
