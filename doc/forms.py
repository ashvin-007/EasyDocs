from django import forms
from .models import DocUpload
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
User=get_user_model()

class docUploadForm(forms.ModelForm):
    class Meta:
        model = DocUpload
        fields = ['title', 'description', 'doc']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Document title'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 4, 'placeholder': 'Enter Document description'}),
        }
    
    def __init__(self, *args, **kwargs):
        super(docUploadForm, self).__init__(*args, **kwargs)
        self.fields['doc'].widget.attrs.update({'class': 'form-control'})
        


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)  # Ensure email is included

    class Meta:
        model = User  # Using Django's built-in User model
        fields = ['username', 'email', 'password1', 'password2']
