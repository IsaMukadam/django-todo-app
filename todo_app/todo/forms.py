from django import forms
from .models import Todo

class TodoForm(forms.ModelForm):
    """
    Form for creating and updating Todo items.

    Inherits from Django's ModelForm to automatically generate
    form fields based on the Todo model.
    """
    class Meta:
        """
        Metadata for TodoForm.

        Specifies the model to base the form on and includes
        all fields of the Todo model in the form.
        """
        model = Todo
        fields = "__all__"