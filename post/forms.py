from django import forms



class CommentForm(forms.Form):
    text=forms.CharField(label='متن',widget=forms.Textarea())








    