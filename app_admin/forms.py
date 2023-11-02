from django import forms
from .models import Category, Food

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['category_name']
        labels = {
            'category_name': 'Kategooria nimi',
        }

class FoodForm(forms.ModelForm):
    class Meta:
        model = Food
        fields = [
            'food_name',
            'food_category',
            'description',
            'full_price',
            'half_price',
            'is_vegetarian',
            'is_vegan',
            'is_gluten_free',
            'is_spicy',
        ]
        labels = {
            'food_name': 'Toidu nimetus',
            'food_category': 'Kategooria',
            'description': 'Kirjeldus',
            'full_price': 'Täishind',
            'half_price': 'Poole hinnaga',
            'is_vegetarian': 'Kas taimetoitlane?',
            'is_vegan': 'Kas vegan?',
            'is_gluten_free': 'Kas gluteenivaba?',
            'is_spicy': 'Kas vürtsikas?',
        }

        widgets = {
            'full_price': forms.NumberInput(attrs={'step': '0.01'}),
            'half_price': forms.NumberInput(attrs={'step': '0.01'}),
        }

    def __init__(self, *args, **kwargs):
        super(FoodForm, self).__init__(*args, **kwargs)
        # Set full_price and half_price fields as not required
        self.fields['full_price'].required = False
        self.fields['half_price'].required = False