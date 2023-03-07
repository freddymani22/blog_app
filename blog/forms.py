from django import forms
from .models import Comment



class CommentForm(forms.ModelForm):
    comment_text = forms.CharField(widget=forms.Textarea(attrs={'rows': 2, 'cols': 50}))
    class Meta:
        model = Comment
        fields = ['comment_text']


