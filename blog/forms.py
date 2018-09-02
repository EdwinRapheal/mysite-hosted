from django import forms

from .models import Post

class PostForm(forms.ModelForm):
	class Meta:
		"""docstring for Meta"""
		model = Post
		fields = ('title', 'text',)