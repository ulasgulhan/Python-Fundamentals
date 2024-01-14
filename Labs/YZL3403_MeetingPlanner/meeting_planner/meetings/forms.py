from django.forms import ModelForm, TextInput, DateInput, TimeInput
from .models import Meeting
from datetime import date
from django.core.exceptions import ValidationError
from string import punctuation


class MeetingForm(ModelForm):
    class Meta:
        model = Meeting
        fields = '__all__'
        widgets = {
            'title': TextInput(attrs={'type': 'text'}),
            'date': DateInput(attrs={'type': 'date'}),
            'start_time': TimeInput(attrs={'type': 'time'}),
            'duration': TextInput(attrs={'type': 'number', 'min': 1, 'max': 4})
        }

    def clean_date(self):
        d = self.cleaned_data.get('date')

        if d < date.today():
            raise ValidationError('Meeting cannot set for the past time!')

        return d

    def clean_title(self):
        title = self.cleaned_data.get('title')

        for c in title:
            if c in punctuation:
                raise ValidationError('Meeting cannot contains punctuation!')

        return title

