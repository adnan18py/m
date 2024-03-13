from django import forms



class CommentForm(forms.Form):
    attrs={'class':'comment_input'}
    text=forms.CharField(label='',widget=forms.Textarea(attrs=attrs))
    








    