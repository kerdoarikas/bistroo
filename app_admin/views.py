from django.views.generic import TemplateView
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Category, Food
from .forms import CategoryForm, FoodForm


class AdminHomeView(TemplateView):
    template_name = 'app_admin/admin_home.html'

class CategoryListView(ListView):
    model = Category
    template_name = 'app_admin/category_list.html'
    context_object_name = 'categories'

class CategoryCreateView(CreateView):
    model = Category
    form_class = CategoryForm
    template_name = 'app_admin/category_create.html'
    success_url = reverse_lazy('app_admin:category_list')

class CategoryUpdateView(UpdateView):
    model = Category
    form_class = CategoryForm
    template_name = 'app_admin/category_update.html'
    success_url = reverse_lazy('app_admin:category_list')

class CategoryDeleteView(DeleteView):
    model = Category
    template_name = 'app_admin/category_delete.html'
    success_url = reverse_lazy('app_admin:category_list')

# TOIDUD

class FoodListView(ListView):
    model = Food
    template_name = 'app_admin/food_list.html'
    context_object_name = 'foods'

class FoodCreateView(CreateView):
    model = Food
    form_class = FoodForm
    template_name = 'app_admin/food_create.html'
    success_url = reverse_lazy('app_admin:food_list')

class FoodDeleteView(DeleteView):
    model = Food
    template_name = 'app_admin/food_delete.html'
    success_url = reverse_lazy('app_admin:food_list')

class FoodUpdateView(UpdateView):
    model = Food
    form_class = FoodForm
    template_name = 'app_admin/food_update.html'
    success_url = reverse_lazy('app_admin:food_list')
