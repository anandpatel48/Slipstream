from django import forms
from .models import Comment

# doing forms for comments
class CommentForm(forms.ModelForm):
    content = forms.CharField(label = "", widget = forms.Textarea(
        attrs = {
            'class': 'form-control',
            'placeholder': 'Comment here!',
            'rows': 2,
            }
    ))
    class Meta:
        model = Comment
        fields = ['content']

    
