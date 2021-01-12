from django import forms

from .models import LectureNotes
from .models import StudentNotes


class LNotesForm(forms.ModelForm):
    class Meta:
        model = LectureNotes
        fields = ('name', 'academician', 'pdf', 'image')


class SNotesForm(forms.ModelForm):
    class Meta:
        model = StudentNotes
        fields = ('name', 'student','pdf','image')