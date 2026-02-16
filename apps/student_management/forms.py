from django import forms
from .models import Student


class StudentForm(forms.ModelForm):
    """Form for creating and editing Student records."""

    def __init__(self, *args, request=None, **kwargs):
        self.request = request
        super().__init__(*args, **kwargs)

    class Meta:
        model = Student
        fields = [
            'first_name',
            'last_name',
            'birth_date',
            'gender',
            'current_academic_level',
            'enrolled_status',
            'photo',
        ]
        widgets = {
            'birth_date': forms.DateInput(attrs={'type': 'date'}),
            'photo': forms.FileInput(attrs={'id': 'photo', 'accept': 'image/jpeg,image/png'}),
        }
