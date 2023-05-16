from django import forms
from .models import Comment



class CommentForm(forms.ModelForm):
    comment_text = forms.CharField(label = '', widget=forms.Textarea(attrs={'rows': 2, 'cols': 25, 'class':'w-auto','placeholder':'Your comments here..'}))
    class Meta:
        model = Comment
        fields = ['comment_text']


