from django import forms
from.models import Post

class PostsForm(forms.ModelForm):
    class Meta:
        model=Post
        fields=("title","slug","image","post_text")
