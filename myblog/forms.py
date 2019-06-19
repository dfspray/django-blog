from django.forms import ModelForm
from myblog.models import Comment
 
class MyCommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ['title', 'text', 'notes']