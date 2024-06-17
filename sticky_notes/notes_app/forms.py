from django.forms import ModelForm
from .models import StickyNote


class StickyNoteForm(ModelForm):
    class Meta:
        model = StickyNote
        exclude = ['user']  # Exclude the user field from the form
