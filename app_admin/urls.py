from django.urls import path
from . import views

app_name = 'app_admin'

urlpatterns = [
    path('', views.AdminHomeView.as_view(), name='admin_home'),
    path('categories/', views.CategoryListView.as_view(), name='category_list'),
    path('categories/create/', views.CategoryCreateView.as_view(), name='category_create'),
    path('categories/update/<int:pk>', views.CategoryUpdateView.as_view(), name='category_update'),
    path('categories/delete/<int:pk>', views.CategoryDeleteView.as_view(), name='category_delete'),
    # FOODS
    path('foods/', views.FoodListView.as_view(), name='food_list'),
    path('foods/create/', views.FoodCreateView.as_view(), name='food_create'),
    path('foods/delete/<int:pk>', views.FoodDeleteView.as_view(), name='food_delete'),
    path('foods/update/<int:pk>', views.FoodUpdateView.as_view(), name='food_update'),
]
