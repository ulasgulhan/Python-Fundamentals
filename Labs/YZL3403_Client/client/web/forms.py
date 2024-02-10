from django.forms import ModelForm, TextInput
from .models import Category
from django.core.exceptions import ValidationError
from string import punctuation


class CategoryForm(ModelForm):
    class Meta:
        model = Category
        fields = '__all__'
        widgets = {
            'name': TextInput(attrs={'type': 'text'}),
            'description': TextInput(attrs={'type': 'text'}),
        }

    def clean_name(self):
        name = self.cleaned_data.get('name')

        for c in name:
            if c in punctuation:
                raise ValidationError('Category name cannot contains punctuation')

        return name

