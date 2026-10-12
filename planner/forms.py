from django import forms
from .models import Assignment

class AssignmentForm(forms.ModelForm):
    class Meta:
        model = Assignment
        fields = ["title", "subject", "due_date"]
        widgets = {
            "title": forms.TextInput(attrs={"placeholder": "e.g. Database project"}),
            "subject": forms.TextInput(attrs={"placeholder": "e.g. Database Systems"}),
            "due_date": forms.DateInput(attrs={"type": "date"}),
        }
        labels = {"title": "Assignment title", "subject": "Subject", "due_date": "Due date"}
